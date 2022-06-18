v = int(input())
v1 = int(input())
v2 = int(input())
n = float(input())

v1_out = v1*n
v2_out = v2*n
total_output = (v1+v2)*n
# print(total_output)
# print(V1_out)
# print(V2_out)

if total_output <= v:
    print(f"The pool is {total_output/v*100}% full. "
      f"Pipe 1: {v1_out/total_output*100:.2f}%. "
      f"Pipe 2: {v2_out/total_output*100:.2f}%.")
else:
    print(f"For {n} hours the pool overflows "
          f"with {total_output-v} liters.")