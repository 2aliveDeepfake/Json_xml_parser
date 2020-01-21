import json # import json module
import os
import shutil

# with statement
# G 드라이브 파일
with open('metadata.json') as json_file:
    json_data = json.load(json_file)

    # 번호 바뀔때마다 metadata.json 해당파일로 바꿔주기
    # 프레임 자르는중 - 13번
    # json parsing video - 13번 해야됨

    # 각 영상별 input ouput 위치
    input_dir = "G:\\Facebook_Dataset_video\\dfdc_train_part_01\\dfdc_train_part_1"
    input_list = os.listdir(input_dir)

    output = "G:\\Facebook_Dataset_video\\dfdc_train_part_01\\"
    # real, fake output 경로
    output_real = output + "dfdc_train_01_real\\"
    output_fake = output + "dfdc_train_01_fake\\"

    # output 폴더 없으면 생성
    if not os.path.exists(output):
        os.mkdir(output)
    if not os.path.exists(output_real):
        os.mkdir(output_real)
    if not os.path.exists(output_fake):
        os.mkdir(output_fake)

    # 영상 개수만큼 반복
    for i in range(len(input_list)):
        #print(input_list[i][0:10])
        # 데이터의 이름이 전부 영어 10자리
        name = input_list[i][0:10]

        json_string = json_data[name+".mp4"]
        #print(json_string["label"])
        # label이 REAL 이면 이동
        if "REAL" in json_string["label"] :
            # print(input_dir + "\\" + str(input_list[i]))
            # print(output_real + str(input_list[i]))
            shutil.move(input_dir + "\\" + input_list[i], output_real + input_list[i])

        # fake 따로 이동 실행
        if "FAKE" in json_string["label"] :
            # print(input_dir + "\\" + str(input_list[i]))
            # print(output_real + str(input_list[i]))
            shutil.move(input_dir + "\\" + input_list[i] , output_fake + input_list[i])

