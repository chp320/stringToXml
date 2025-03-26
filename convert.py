import xml.etree.ElementTree as ET
from xml.dom import minidom
 
# txt 파일 읽기
with open('sample.txt','r') as file:
  lines = file.readlines()

# xml 구조 생성
root = ET.Element("records")

# 첫 번째 줄은 헤더이므로 건너뜀
for line in lines[1:]:
  # 쉼표로 구분해서 데이터 추출
  id, first_name, last_name, email, gender, ip_address = line.strip().split(',')

  # record 요소 생성
  record = ET.SubElement(root, "record")
  ET.SubElement(record, "id").text = id
  ET.SubElement(record, "first_name").text = first_name
  ET.SubElement(record, "last_name").text = last_name
  ET.SubElement(record, "email").text = email
  ET.SubElement(record, "gender").text = gender
  ET.SubElement(record, "ip_address").text = ip_address

# xml 내용을 문자열로 변환
xml_str = ET.tostring(root, encoding='utf-8').decode('utf-8')

# xml 선언 추가
xml_str = '<?xml version="1.0" encoding="utf-8"?>\n' + xml_str

# 문자열을 포맷팅해서 보기 좋게 만들기
pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="")

# 포맷팅된 xml 을 파일로 저장
with open("data.xml","w",encoding='utf-8') as xml_file:
  # minidom 의 toprettyxml 은 추가적인 빈 줄을 생성하므로 이를 제거
  lines = pretty_xml.splitlines()
  lines = [line for line in lines if line.strip()]  # 빈줄 제거

  # 최상위 <records> 요소는 들여쓰기 하지 않음
  formatted_lines = [lines[0]]

  
  # 들여쓰기를 위한 수정
  for line in lines[1:]:
    if line.startswith("<records>") or line.startswith("</records>"):
      formatted_lines.append(line)  # <record>, </record> 는 기본 들여쓰기
    elif line.startswith("<record>") or line.startswith("</record"):
      formatted_lines.append("\t" + line)
    else:
      formatted_lines.append("\t\t" + line)  # 그외 줄은 그대로

  xml_file.write('\n'.join(formatted_lines))
