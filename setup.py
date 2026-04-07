from setuptools import setup


setup(
    name="adversarial-skills",
    version="0.1.0",
    py_modules=["server", "bundled_skills"],
    install_requires=["mcp"],
    entry_points={
        "console_scripts": [
            "adversarial-skills=server:main",
        ]
    },
)