'''
txt를 읽어 한국어와 영어 명칭을 각각 키와 값으로 갖는
딕셔너리를 생성하는 코드를 작성하세요.
'''

txt = '''신경발달장애 Neurodevelopmental Disorders
조현병 스펙트럼 및 기타 정신병적 장애 Schizophrenia Spectrum and Other Psychotic Disorders
양극성 및 관련 장애 Bipolar and Related Disorders
우울장애 Depressive Disorders
불안장애 Anxiety Disorder
강박 및 관련 장애 Obsessive－Compulsive and Related Disorders
외상 및 스트레스 관련 장애 Trauma－and Stressor－Related Disorders
해리장애 Dissociative Disorders
신체증상 및 관련 장애 Somatic Symptom and Related Disorders
급식 및 섭식장애 Feeding and Eating Disorders
배설장애 Elimination Disorders
수면－각성 장애 Sleep－Wake Disorders
성기능부전 Sexual Dysfunctions
성별 불쾌감 Gender Dysphoria
파괴적, 충동조절 및 품행 장애 Disruptive, Impulse－Control, and Conduct Disorders
물질관련 및 중독 장애 Substance－Related and Addictive Disorders
신경인지장애 Neurocognitive Disorders
성격장애 Personality Disorders
변태성욕장애 Paraphilic Disorders
기타 정신질환 Other Mental Disorders'''

disorders = dict()

is_eng = lambda x: ord('A') <= ord(x) <= ord('Z') or ord('a') <= ord(x) <= ord('z')

for x in txt.split('\n'):
    i = 0
    while not is_eng(x[i]):
        i += 1
    else:
        ko, en = x[:i - 1], x[i:]
        disorders[ko] = en

print(disorders)
    
