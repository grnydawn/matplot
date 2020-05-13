"matplot setup module."

def main():

    from setuptools import setup
    from matplot import MatPlot

    app_requires = MatPlot.get("app_requires", [])
    install_requires = ["microapp>=0.1.11"] + app_requies

    setup(
        name=MatPlot._name_,
        version=MatPlot._version_,
        description=MatPlot._description_,
        long_description=MatPlot._long_description_,
        author=MatPlot._author_,
        author_email=MatPlot._author_email_,
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "Topic :: Scientific/Engineering",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        keywords="microapp matplot",
        packages=["matplot"],
        include_package_data=True,
        install_requires=install_requires,
        entry_points={"microapp.apps": "matplot = matplot"},
        project_urls={
            "Bug Reports": "https://github.com/grnydawn/matplot/issues",
            "Source": "https://github.com/grnydawn/matplot",
        }
    )

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()
