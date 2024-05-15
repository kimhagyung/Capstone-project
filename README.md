# CNN과 히스토그램을 사용한 이미지 분류 및 추천 시스템
### **시스템 개발의 배경 및 필요성**
- 현행 비즈니스 상황
    - 2023년 현재, 바디 프로필과 스튜디오 사진 촬영이 2030 세대를 중심으로 유행하고 있다.
스튜디오 사진 촬영에 대한 의향이 전체 응답자 중 9명 중 8명이라는 결과는 스튜디오 사진의 인기가 높다는 것을 시사한다. 
또한, 다양한 콘셉트로 스튜디오 사진을 찍는 사람들의 증가는 사진 촬영을 통해 자신의 개성이나 스타일을 표현하고자 하는 데에 관심이 높아지고 있다는 것을 시사한다. 이는 스튜디오 사진이 예술적 표현 수단으로서도 사용되고 있음을 나타낸다.

- 현행 시스템의 문제점
    - 사진을 수요하는 고객 관점에서 방대한 정보와 광고로 인해 상단에 노출되는 기업들을 명확한 기준으로 자신의 목적에 맞게 필터링하기 힘들다.
시스템 내에서 분류되지 않는 이미지들이 적절하지 않은 카테고리에 저장되는 경우가 있어, 사용자들은 원하는 카테고리의 이미지를 찾는 데 어려움을 겪는다.
사진작가들은 자신의 작품을 더 많은 관객과 잠재적인 고객들에게 보여주고자 한다. 그러나 기존의 소셜 미디어 플랫폼은 모든 유형의 작가와 사진에 중점을 두기 어려울 수 있다.
사진을 수요하는 고객은 자신의 요구사항과 취향에 부합하는 사진작가를 찾기 어렵다고 느낄 수 있다.

### **프로젝트 목적 및 목표**

- 시스템의 목적
  1. 시스템은 작가들이 사진을 업로드할 수 있는 환경을 제공해준다.
시스템은 카테고리별로 추천 기준에 따라 각 고객에게 사진을 추천해준다.
  2. 시스템은 카테고리별로 추천 기준에 따라 각 고객에게 사진을 추천해준다
 
- 시스템의 목표
  1. 카테고리별 사진을 분류해서 사진들을 한눈에 볼 수 있다.
  2. 카테고리별로 고객에게 정확한 정보를 제공한다.
<br>

### **프로젝트 선택 이유** 
- 웹에서의 서버와 클라이언트의 동작 과정을 배우고 인공지능을 사용해 웹 사이트에 적용 해보고 싶어 선택
<br>

### **역할**
- 리액트를 활용하여 프론트엔드를 구성(하지만 주로 백엔드 위주)
- Node.js를 이용하여 API 및 Ajax 통신을 구현
- Docker 컨테이너 내에서 DB 테이블을 생성하고 관리 및 Docker Hub에 이미지 배포
(https://hub.docker.com/repository/docker/rlagkrud/capstone/general)
- 네이버 로그인 API를 통한 사용자 인증 기능을 구현
- CNN 모델 학습 및 데이터셋 수집(다같이)
- 완성된 모델 웹페이지 적용(TensorFlow.js 사용)
- 이미지분류를 위한 히스토그램 적용 
<br>

### **시스템 개발 환경 및 언어**

  <img width="700" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/ba2a27a5-3d75-4c51-aabd-9c8662b761ad">
 

### **기술 설명 및 핵심 내용**

- 딥러닝_ CNN(Convolutional Neural Network)
    - CNN은 이미지의 공간적인 구조를 이용하여 특징을 추출하고 이미지 내의 작은 부분들을 학습시키고 이를 조합하여 더 복잡한 특징을 추출하는 방식으로 동작하여 레이블별로 이미지를 분류.
    - 작가가 업로드할 때 해당 사진의 카테고리를 자동으로 분류하기 위해 사용
- 히스토그램
  - 이미지의 픽셀값을 밝기로 변환하고, 각 밝기 값 의 빈도를 히스토그램 배열로 구성
  - 사용자가 사진을 업로드하면 사이트에 업로드되어 있는 사진들 중에 비슷한 색감을 가진 상위 3 장을 추천해주기 위해 사용. 
<br>

### **시스템 구상도**

<img width="404" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/f21f0671-2744-496d-8c07-ea7611419615">        
<br>

### **전체 기능**

<img width="500" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/9ecf0e61-d124-4c38-9950-731847d34eed">          
      
 
### **시스템 개발 범위**      

<img width="500" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/cffd8aa6-7cc8-41fe-a112-68ebb6ad3560">      


  
###  **클래스 다이어그램**

<img width="700" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/05861882-2dd9-46f0-9230-729e962dbf24">

### **시스템 개발 관리**

<img width="900" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/9d3a592f-853b-4e70-a5a5-6336fb36afd8">


### **최종화면**

![image](https://github.com/kimhagyung/Capstone-project/assets/88253931/caf7918f-4dd1-48e2-8486-73ffaf87a181)<hr>
![image](https://github.com/kimhagyung/Capstone-project/assets/88253931/6e3ea5a4-3a0d-4c4c-831b-a5b2705675e6)<hr>
![image](https://github.com/kimhagyung/Capstone-project/assets/88253931/01dce05e-6ab2-4014-9a7b-acdf11dd26bb)<hr>
![image](https://github.com/kimhagyung/Capstone-project/assets/88253931/e3deb653-6332-4692-959d-9451a7c39a5d)<hr>
![image](https://github.com/kimhagyung/Capstone-project/assets/88253931/1144a7fe-084c-43f0-92cf-cb02a9b6f6c1)<hr>
![image](https://github.com/kimhagyung/Capstone-project/assets/88253931/77213e8c-3127-4252-ad40-bfc21cca6e77)<hr>
![image](https://github.com/kimhagyung/Capstone-project/assets/88253931/04f1b35e-002d-4d72-81d6-f841192698df)<hr>
![image](https://github.com/kimhagyung/Capstone-project/assets/88253931/4bf5d8db-f5a1-441f-90e0-1f0aab01dc1d)<hr>
![image](https://github.com/kimhagyung/Capstone-project/assets/88253931/a2620a58-6c61-4dc4-9801-2fdba8cdef2b)<hr>
![image](https://github.com/kimhagyung/Capstone-project/assets/88253931/9a3763a7-f613-4102-836f-33ca148f8ead)<hr>
![image](https://github.com/kimhagyung/Capstone-project/assets/88253931/07f850c4-e04c-4af0-957a-2040c544cda7)<hr>













