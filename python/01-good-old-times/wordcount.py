#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, string

# 중간의 '보조 기억 장치'를 처리하는 편의 함수
def touchopen(filename, *args, **kwargs):
	try:
		os.remove(filename)
	except OSError:
		pass
	open(filename, "a").close() # 파일을 '수정'한다
	return open(filename, *args, **kwargs)

# 메모리 제약은 크기가 1024이하다
data = []
# 우리는 행운아다:
# 의미 없는 단어는 556자에 불과하고 모든 줄은
# 80자 미만이므로 문제를 단순화할 수 있다.
# 즉, 한 번에 한 줄씩 입력받아 처리하는 동안
# 의미 없는 단어를 메모리에 둘 수 있다.
# 이 두 가정이 유효하지 않으면 알고리즘을
# 상당히 변경해야 한다.

# 전체 전략: (부분 1) 입력 파일을 읽어 단어를 세고
# 보조 기억 장치(파일)에 횟수를 증가/저장한다.
# (부분 2) 보조 기억 장치에서 가장 빈도가 높은 단어 25개를 찾는다.

# 부분 1:
# - 입력 파일에서 한 번에 한 줄씩 읽는다.
# - 문자를 걸러낸 후 소문자로 정규화한다.
# - 단어를 식별하고 파일에서 해당하는 횟수를 증가시킨다.

# 의미 없는 단어 목록을 읽어 들인다.
f = open('./data/stop_words.txt')
data = [f.read(1024).split(',')]
f.close
