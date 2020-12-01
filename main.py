import os
import sys


def main():
    organiser = sys.argv[2]
    project_name = sys.argv[1]
    usage = "Usage: gitupdate [project name] [account]\n"

    os.system("rm -rf {}".format(project_name))
    os.system("git clone https://github.com/{}/{}".format(organiser, project_name))


if __name__ == '__main__':
    main()
