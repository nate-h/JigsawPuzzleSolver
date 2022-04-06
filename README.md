# JigsawPuzzleSolver

The ultimate goal of this program is to take a pic of unconnected puzzle pieces
on a green screen and use computer vision to render the fully assembled
puzzle.

Steps to get environment up
---------------------------

```sh
    virtualenv -p python3 JigsawPuzzleSolver
    source ./JigsawPuzzleSolver/bin/activate
    pip install -r requirements.txt
    JigsawPuzzleSolver/bin/jupyter notebook
    python -m ipykernel install --user --name=JigsawPuzzleSolver
```