import os
from PyPDF2 import PdfReader

def clean_text(text):
    # 서로게이트 페어와 같은 잘못된 유니코드 문자 제거
    return text.encode('utf-8', errors='ignore').decode('utf-8')

def pdf_to_txt(input_path, output_path):
    # PDF 파일 읽기
    reader = PdfReader(input_path)
    
    # 텍스트 추출
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    # 텍스트 정제
    cleaned_text = clean_text(text)
    
    # 텍스트 파일로 저장
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_text)

def process_all_pdfs():
    # 입력 및 출력 디렉토리 설정
    input_dir = "input"
    output_dir = "output"
    
    # 출력 디렉토리가 없으면 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # input 디렉토리의 모든 PDF 파일 처리
    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf') or filename.endswith('.PDF'):
            input_path = os.path.join(input_dir, filename)
            output_filename = f"output_{os.path.splitext(filename)[0]}.txt"
            output_path = os.path.join(output_dir, output_filename)
            
            print(f"변환 중: {filename}")
            try:
                pdf_to_txt(input_path, output_path)
                print(f"완료: {output_filename}")
            except Exception as e:
                print(f"오류 발생 ({filename}): {str(e)}")

if __name__ == "__main__":
    process_all_pdfs()
