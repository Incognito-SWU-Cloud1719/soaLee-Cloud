from setuptools import setup, find_packages

setup(name='sftpp', 
      # 프로젝트 명을 입력합니다.
      version='0.0.1', 
      # 프로젝트 버전을 입력합니다.
      url='https://github.com/Incognito-SWU-Cloud1719', 
      # 홈페이지 주소를 입력합니다.
      author='Cloud1719', 
      # 프로젝트 담당자 혹은 작성자를 입력합니다.
      description='Can use it to install sftp port service from Python.', 
      # 프로젝트에 대한 간단한 설명을 입력합니다.
      packages=find_packages(exclude=['tests']), 
      # 기본 프로젝트 폴더 외에 추가로 입력할 폴더를 입력합니다.
      long_description=open('README.md').read(), 
      # 프로젝트에 대한 설명을 입력합니다. 보통 README.md로 관리합니다.
      long_description_content_type='text/markdown', 
      # 마크다운 파일로 description를 지정했다면 text/markdown으로 작성합니다.
      install_requires=['cython'],
      # 설치시 설치할 라이브러리를 지정합니다.
      # cython은 CPython 확장 모듈을 손쉽게 생성하도록 고안된 컴파일 언어
      zip_safe=False,
      classifiers=[
          'License :: OSI Approved :: MIT License'
      ] 
      # 기본적으로 LICENSE 파일이 있다고 하더라도 명시적으로 적어 놓는 것이 좋습니다.
)