set -e

eval "$(conda shell.bash hook)"

conda activate Xanylabeling

cd /home/ngochdm/Desktop/github/Xanylabeling-customize/

if ! command -v pyrcc5 >/dev/null 2>&1; then
    echo "pyrcc5 not found. Activate an environment with PyQt5 installed." >&2
    exit 1
fi

pyrcc5 -o anylabeling/resources/resources.py anylabeling/resources/resources.qrc
