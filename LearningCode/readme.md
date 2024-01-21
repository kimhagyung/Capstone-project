합성곱 신경망(CNN, Convolutional Neural Network)이란? 
CNN은 이미지를 분석하기 위한 패턴을 찾는데 유용한 알고리즘이며, 이미지를 직접 학습하고 패턴을 사용해 이미지를 분류한다.

사용된 CNN 구조 설명 
- 총 데이터 셋 : 4987장
-> 수집 출처 : SNS, naver, google 등의 웹사이트

exif.py 
- 이미지의 Exchangeable image file format (EXIF) 메타데이터를 제거하는 기능을 수행하여 이미지 전처리 작업 수행 

- Conv2D(16, 3, padding='same', activation='relu', input_shape=(img_height, img_width, 3)):
3x3 크기의 커널을 사용하여 16개의 필터로 이미지에 합성곱을 수행합니다.
'same' 패딩을 사용하여 입력과 출력의 크기를 동일하게 유지합니다.
ReLU 활성화 함수를 사용하여 비선형성을 도입합니다.
입력 이미지의 크기는 (400, 500, 3)입니다.

MaxPooling2D():
2x2 크기의 맥스 풀링을 수행하여 공간 차원을 줄입니다.
최대 풀링은 각 영역에서 최댓값을 추출하는 연산을 수행합니다.

Conv2D(32, 3, padding='same', activation='relu'):
3x3 크기의 커널을 사용하여 32개의 필터로 이미지에 합성곱을 수행합니다.
'same' 패딩을 사용하여 입력과 출력의 크기를 동일하게 유지합니다.
ReLU 활성화 함수를 사용하여 비선형성을 도입합니다.

MaxPooling2D():
2x2 크기의 맥스 풀링을 수행하여 공간 차원을 줄입니다.

Conv2D(64, 3, padding='same', activation='relu'):
3x3 크기의 커널을 사용하여 64개의 필터로 이미지에 합성곱을 수행합니다.
'same' 패딩을 사용하여 입력과 출력의 크기를 동일하게 유지합니다.
ReLU 활성화 함수를 사용하여 비선형성을 도입합니다.

MaxPooling2D():
2x2 크기의 맥스 풀링을 수행하여 공간 차원을 줄입니다.

Dropout(0.2):
20%의 드롭아웃을 적용하여 과적합을 방지합니다.

Flatten():
3D 출력을 1D로 평탄화합니다.

Dense(128, activation='relu'):
128개의 뉴런으로 이루어진 완전 연결 레이어입니다.
ReLU 활성화 함수를 사용하여 비선형성을 도입합니다.

layers.Dense(num_classes, activation='softmax') 
출력 레이어로, 클래스의 수에 해당하는 5개의 뉴런 수를 가집니다. softmax 활성화 함수 적용
