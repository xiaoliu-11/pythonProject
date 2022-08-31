from cffi.backend_ctypes import unicode

url = "https://tss.ojmsfec.cn/91tv/91tv/X5Exprclguxohsybtkhtlmfdmfeblx/hls/1/index0.ts"
iv = "f507f232153c2fb52903ed0c0781a146"
print(url.split('/')[-1])
print(iv[:16].encode())

# b'8g>\xd3\x1b<\x04\xae[f7TJ\xbeM\xb1'
s = '8g>\xd3\x1b<\x04\xae[f7TJ\xbeM\xb1'
ss = s.encode('raw_unicode_escape')
print(ss)  # 结果：b'\xe9\x9d\x92\xe8\x9b\x99\xe7\x8e\x8b\xe5\xad\x90'
sss = ss.decode("ISO-8859-1","ignore")
print(sss)