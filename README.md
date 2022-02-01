# Challenge 9: End-to-End Image Processing and Analysis with Galaxy

## Description
As the multiplex tissue imaging field continues to grow, modern computational infrastructure is required for the field to meet key data analysis needs. These needs include scalable and standardized workflows to process large datasets, automated and reproducible analyses for harmonized and comparing results, and a graphical user interface that makes these analyses accessible to all scientists regardless of their informatics expertise. To meet these needs, we have developed a tool suite for end-to-end multiplex tissue imaging for the Galaxy computational workbench. Galaxy (https://galaxyproject.org) is a web-based platform used daily across the world by thousands of scientists for all kinds of large-scale biomedical analyses. The Galaxy community is expanding its set of imaging algorithms and methods, but integration and development of new tools, methods, workflows is still needed.

## Subchallenges
1. Bring your algorithm/method or choose from a predefined list and integrate it into Galaxy.
2. Bring your own data and process it with the Galaxy tool suite.
3. Build your own Galaxy workflow to suit the data type/analysis you need.

## Installation
Having a local installation of galaxy is highly recommended for this challenge. Clone the repo and follow the instructions on the [Galaxy Project Github](https://github.com/galaxyproject/galaxy) Github. 
```
git clone https://github.com/galaxyproject/galaxy.git
cd galaxy
sh ./run.sh
```

## Data
Example datasets (OME-TIFF registered images) will be provided on Synapse [syn26848767](https://www.synapse.org/#!Synapse:syn26848767) and the test Galaxy instances (TBD).

## Testing and Deployment
Testing of tools can be completed using a local instance of Galaxy or using Planemo (see docs below). Cloud instances installed with all MCMICRO tools will be available for deployment and additional testing of tools.

## Galaxy Documentation & Tutorials
### Galaxy Basics
 - [Galaxy Intro](https://training.galaxyproject.org/training-material/topics/introduction/slides/introduction.html)
 - [Galaxy 101 tutorial](https://training.galaxyproject.org/training-material/topics/introduction/tutorials/galaxy-intro-101/tutorial.html)

### Galaxy Tool Development
 - [Galaxy Tool Development Docs](https://docs.galaxyproject.org/en/latest/dev/schema.html)
 - [Planemo for Building Galaxy Tools](https://planemo.readthedocs.io/en/latest/writing.html)

### Galaxy for Image Processing
 - [MCMICRO website](https://mcmicro.org/)
 - [Imaging Tutorials](https://training.galaxyproject.org/training-material/topics/imaging/)