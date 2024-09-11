from rich import print as rprint
import tomllib
from pathlib import Path

pyproject_path = Path(__file__).parent.parent / "pyproject.toml"


def get_current_version():
	with open(pyproject_path, "rb") as f:
		project_config = tomllib.load(f)
	return project_config["tool"]["poetry"]["version"]


def display_banner():
	current_version = get_current_version()
	rprint(f"""[magenta]
                        █████╗ ██████╗  █████╗        ██████╗ ██╗     ██╗      ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗
                        ██╔══██╗██╔══██╗██╔══██╗      ██╔════╝██║     ██║      ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
                        ███████║██████╔╝███████║█████╗██║     ██║     ██║█████╗███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
                        ██╔══██║██╔══██╗██╔══██║╚════╝██║     ██║     ██║╚════╝╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
                        ██║  ██║██████╔╝██║  ██║      ╚██████╗███████╗██║      ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
                        ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝       ╚═════╝╚══════╝╚═╝      ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                        V{current_version}
                                                                        by
                                                                        @poneoneo

        """)


if __name__ == "__main__":
	display_banner()
