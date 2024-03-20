from setuptools import setup, find_packages

HYPEN_E_DOT='-e .'

def get_requirements(filename)->list[str]:
    '''Read requirements file and return list of requirements'''	
    requirements=[]
    with open(filename) as file:
        for line in file:
            requirements=file.readline()
            requirements=[req.replace("\n","") for req in requirements]
            
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    return requirements
  

setup (
  name='boston-housing-prices',
  version='0.1',
  author='Curtney Jacobs',
  author_email='curtneyjacobs@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt')
  )