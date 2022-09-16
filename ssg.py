import typer

from ssg.site import Site


def main(source: str = "content", dest: str = "dist") -> None:
    config = {"source": source, "dest": dest}
    Site(**config).build()


if __name__ == "__main__":
    typer.run(main)
