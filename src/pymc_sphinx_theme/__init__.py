"""A thin sphinx theme to customize pydata-sphinx-theme consistently cross PyMC websites."""

__version__ = "0.14.0"

from pathlib import Path


# For more details, see:
# https://www.sphinx-doc.org/en/master/development/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    theme_path = Path(__file__).parent.resolve()
    app.add_html_theme("pymc_sphinx_theme", str(theme_path))
    app.config.templates_path.append(str(theme_path / "components"))
    return {"version": __version__, "parallel_read_safe": True}
