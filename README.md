# CNN과 히스토그램을 사용한 이미지 분류 및 추천 시스템

**시스템 개발의 배경 및 필요성**
- 현행 비즈니스 상황
    - 2023년 현재, 바디 프로필과 스튜디오 사진 촬영이 2030 세대를 중심으로 유행하고 있다.
스튜디오 사진 촬영에 대한 의향이 전체 응답자 중 9명 중 8명이라는 결과는 스튜디오 사진의 인기가 높다는 것을 시사한다. 
또한, 다양한 콘셉트로 스튜디오 사진을 찍는 사람들의 증가는 사진 촬영을 통해 자신의 개성이나 스타일을 표현하고자 하는 데에 관심이 높아지고 있다는 것을 시사한다. 이는 스튜디오 사진이 예술적 표현 수단으로서도 사용되고 있음을 나타낸다.

- 현행 시스템의 문제점
    - 사진을 수요하는 고객 관점에서 방대한 정보와 광고로 인해 상단에 노출되는 기업들을 명확한 기준으로 자신의 목적에 맞게 필터링하기 힘들다.
시스템 내에서 분류되지 않는 이미지들이 적절하지 않은 카테고리에 저장되는 경우가 있어, 사용자들은 원하는 카테고리의 이미지를 찾는 데 어려움을 겪는다.
사진작가들은 자신의 작품을 더 많은 관객과 잠재적인 고객들에게 보여주고자 한다. 그러나 기존의 소셜 미디어 플랫폼은 모든 유형의 작가와 사진에 중점을 두기 어려울 수 있다.
사진을 수요하는 고객은 자신의 요구사항과 취향에 부합하는 사진작가를 찾기 어렵다고 느낄 수 있다.

**프로젝트 목적 및 목표**

- 시스템의 목적
  1. 시스템은 작가들이 사진을 업로드할 수 있는 환경을 제공해준다.
시스템은 카테고리별로 추천 기준에 따라 각 고객에게 사진을 추천해준다.
  2. 시스템은 카테고리별로 추천 기준에 따라 각 고객에게 사진을 추천해준다
 
- 시스템의 목표
  1. 카테고리별 사진을 분류해서 사진들을 한눈에 볼 수 있다.
  2. 카테고리별로 고객에게 정확한 정보를 제공한다.
 
  시스템 개발 환경 및 언어

  <img width="414" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/ba2a27a5-3d75-4c51-aabd-9c8662b761ad">

**기술 설명 및 핵심 내용**
- 딥러닝_ CNN(Convolutional Neural Network)
    - CNN은 이미지의 공간적인 구조를 이용하여 특징을 추출하고 이미지 내의 작은 부분들을 학습시키고 이를 조합하여 더 복잡한 특징을 추출하는 방식으로 동작하여 레이블별로 이미지를 분류.
    - 작가가 업로드할 때 해당 사진의 카테고리를 자동으로 분류하기 위해 사용
- 히스토그램
  - 이미지의 픽셀값을 밝기로 변환하고, 각 밝기 값 의 빈도를 히스토그램 배열로 구성
  - 사용자가 사진을 업로드하면 사이트에 업로드되어 있는 사진들 중에 비슷한 색감을 가진 상위 3 장을 추천해주기 위해 사용. 

**시스템 구상도**

<img width="404" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/f21f0671-2744-496d-8c07-ea7611419615">        

**전체 기능**

<img width="500" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/9ecf0e61-d124-4c38-9950-731847d34eed">          
      
<br> **시스템 개발 범위**      

<img width="500" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/cffd8aa6-7cc8-41fe-a112-68ebb6ad3560">      


<br>  **클래스 다이어그램**

<img width="700" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/05861882-2dd9-46f0-9230-729e962dbf24">

<br> **시스템 개발 관리**

<img width="900" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/9d3a592f-853b-4e70-a5a5-6336fb36afd8">


<br> **최종화면**

<img width="700" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/ac1d648e-aed4-4f16-bdc5-5cad65578d9a"> 
 <br> <img width="700" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/c4d0f88b-1eee-49c1-bf2d-fe75d1bdd709">
 <br> <img width="700" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/aae49795-e3b9-416d-842c-a1ae64c94b8a">
<img width="700" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/29320d57-5566-4cef-839f-f704dfd79684">
<img width="700" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/4d661816-df5f-4f08-b662-e51a7c659bd4">
<img width="700" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/929d4671-3b6c-4324-b45a-650e1e497290">
<img width="700" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/bfb94b95-4dd1-4a8b-af3b-513d9c4644c2">
<img width="700" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/664f60ff-f295-41df-b44b-0f7657e367af">
<img width="700" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/68aad8b0-e1e8-4aff-a5c3-fa5c1aa01280">
<img width="700" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/9f1dbbd2-4993-41c6-a67e-3a0a868d8eec">
<img width="700" alt="image" src="https://github.com/kimhagyung/Capstone-project/assets/88253931/45d2cde8-3afb-4641-9ad4-3c6100fe50b6">












