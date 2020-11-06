import tensorflow as tf

hello = tf.constant('Hello World!')
s = tf.Session()
print(s.run(hello))




'''
import cpuid

print("Vendor ID         : %s" % cpuid.cpu_vendor())
print("CPU name          : %s" % cpuid.cpu_name())
print("Microarchitecture : %s%s" % cpuid.cpu_microarchitecture())
print("Vector instructions supported:")
print("SSE       : %s" % cpuid._is_set(1, 3, 25))
print("SSE2      : %s" % cpuid._is_set(1, 3, 26))
print("SSE3      : %s" % cpuid._is_set(1, 2, 0))
print("SSSE3     : %s" % cpuid._is_set(1, 2, 9))
print("SSE4.1    : %s" % cpuid._is_set(1, 2, 19))
print("SSE4.2    : %s" % cpuid._is_set(1, 2, 20))
print("SSE4a     : %s" % cpuid._is_set(0x80000001, 2, 6))
print("AVX       : %s" % cpuid._is_set(1, 2, 28))
print("AVX2      : %s" % cpuid._is_set(7, 1, 5))
print("BMI1      : %s" % cpuid._is_set(7, 1, 3))
print("BMI2      : %s" % cpuid._is_set(7, 1, 8))
'''