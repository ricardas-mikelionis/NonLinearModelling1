import math


def addition(kv1, kv2):
        if len(kv1) != 4 or len(kv2) != 4:
            print("Error: one or both variables are not quaternion")
            res = [0, 0, 0, 0]
            return res
        else:
            res = [kv1[0]+kv2[0], kv1[1]+kv2[1], kv1[2]+kv2[2], kv1[3]+kv2[3]]
            return res


def subtraction(kv1, kv2):
        if len(kv1) != 4 or len(kv2) != 4:
            print("Error: one or both variables are not quaternion")
            res = [0, 0, 0, 0]
            return res
        else:
            res = [kv1[0]-kv2[0], kv1[1]-kv2[1], kv1[2]-kv2[2], kv1[3]-kv2[3]]
            return res


def multiplication(kv1, kv2):
    if len(kv1) != 4 or len(kv2) != 4:
        print("Error: one or both variables are not quaternion")
        res = [0, 0, 0, 0]
        return res
    else:
        w1 = kv1[0] * kv2[0] - kv1[1] * kv2[1] - kv1[2] * kv2[2] - kv1[3] * kv2[3]
        w2 = kv1[1] * kv2[0] + kv1[0] * kv2[1] - kv1[3] * kv2[2] + kv1[2] * kv2[3]
        w3 = kv1[2] * kv2[0] + kv1[3] * kv2[1] + kv1[0] * kv2[2] - kv1[1] * kv2[3]
        w4 = kv1[3] * kv2[0] - kv1[2] * kv2[1] + kv1[1] * kv2[2] + kv1[0] * kv2[3]
        res = [w1, w2, w3, w4]
        return res


def absquat(kv):
    if len(kv) != 4:
        print("Error: one or both variables are not quaternion")
        res = [0, 0, 0, 0]
        return res
    else:
        res = math.sqrt(kv[0] ** 2 + kv[1] ** 2 + kv[2] ** 2 + kv[3] ** 2)
        return res

