import shutil
import sys
import os
import tempfile
import zipfile
import typing as tp


from satella.files import find_files


def find_so(*path) -> tp.List[str]:
    return list(find_files(os.path.join(*path), r'(.*)\.so', scan_subdirectories=True))


def find_all(*path) -> tp.List[str]:
    return list(find_files(os.path.join(*path), r'(.*)', scan_subdirectories=True))


def process_wheel(path):
    cwd = os.getcwd()

    tempdir = tempfile.mkdtemp()
    os.chdir(tempdir)

    if path.startswith('/'):
        path_to_file = path
    else:
        path_to_file = os.path.join(cwd, path)

    with zipfile.ZipFile(path_to_file, 'rb') as zip_f:
        zip_f.extractall()

    for so_file in find_so('.'):
        os.system('strip %s' % (so_file, ))

    with zipfile.ZipFile(path_to_file, 'wb') as zip_f:
        for file in find_all('.'):
            zip_f.write(file, compress_type=zipfile.ZIP_DEFLATED)


def run():
    try:
        path = sys.argv[1]
    except IndexError:
        print('Usage:'
              'doctor-wheel <path to whl1 file> <path to whl2 file> ...'
              'Files will be updated in place.', file=sys.stderr)
        sys.exit(1)

    if not shutil.which('strip'):
        print('This required strip to be installed', file=sys.stderr)
        sys.exit(1)

    for wheel_path in sys.argv[1:]:
        if not os.path.isfile(wheel_path):
            print('%s is not a file aborting' % (wheel_path, ), sys=sys.stderr)
            sys.exit(1)

    for wheel_path in sys.argv[1:]:
        process_wheel(wheel_path)

    sys.exit(0)
