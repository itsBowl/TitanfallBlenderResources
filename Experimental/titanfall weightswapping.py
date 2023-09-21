import bpy

weightList = [

    #Left side
    ['def_l_clav', 'DEF-shoulder.L'],
    ['def_l_shoulder', 'DEF-upper_arm.L'],
    ['def_l_shoulderTwist', 'def_l_shoulderTwist'], #Undefined in Rigify
    ['def_l_elbowB', 'def_l_elbowB'],               #Undefined in Rigify
    ['def_l_shoulderMid', 'DEF-upper_arm.L.001'],
    ['def_l_elbow', 'DEF-forearm.L'],
    ['def_l_forearm', 'DEF-forearm.L.001'],
    ['def_l_wrist', 'DEF-hand.L'],
    ['def_l_finIndexA', 'DEF-f_index.01.L'],
    ['def_l_finIndexB', 'DEF-f_index.02.L'],
    ['def_l_finIndexC', 'DEF-f_index.03.L'],
    ['def_l_finMidA', 'DEF-f_middle.01.L'],
    ['def_l_finMidB', 'DEF-f_middle.02.L'],
    ['def_l_finMidC', 'DEF-f_middle.03.L'],
    ['def_l_finThumbA', 'DEF-thumb.01.L'],
    ['def_l_finThumbB', 'DEF-thumb.02.L'],
    ['def_l_finThumbC', 'DEF-thumb.03.L'],
    ['def_l_finRingCarpal', 'def_l_finRingCarpal'], #Undefined in Rigify
    ['def_l_finRingA', 'DEF-f_ring.01.L'],
    ['def_l_finRingB', 'DEF-f_ring.02.L'],
    ['def_l_finRingC', 'DEF-f_ring.03.L'],
    ['def_l_finPinkyA', 'DEF-f_pinky.01.L'],
    ['def_l_finPinkyB', 'DEF-f_pinky.02.L'],
    ['def_l_finPinkyC', 'DEF-f_pinky.03.L'],
    ['def_l_thigh', 'DEF-thigh.L'],
    ['def_l_knee', 'DEF-shin.L'],
    ['def_l_kneeB', 'def_l_kneeB'],
    ['def_l_ankle', 'DEF-foot.L'],
    ['def_l_ball', 'DEF-toe.L'],
    #Right Side
    ['def_r_clav', 'DEF-shoulder.R'],
    ['def_r_shoulder', 'DEF-upper_arm.R'],
    ['def_r_shoulderTwist', 'def_r_shoulderTwist'], #Undefined in Rigify
    ['def_r_elbowB', 'def_r_elbowB'],               #Undefined in Rigify
    ['def_r_shoulderMid', 'DEF-upper_arm.R.001'],
    ['def_r_elbow', 'DEF-forearm.R'],
    ['def_r_forearm', 'DEF-forearm.R.001'],
    ['def_r_wrist', 'DEF-hand.R'],
    ['def_r_finIndexA', 'DEF-f_index.01.R'],
    ['def_r_finIndexB', 'DEF-f_index.02.R'],
    ['def_r_finIndexC', 'DEF-f_index.03.R'],
    ['def_r_finMidA', 'DEF-f_middle.01.R'],
    ['def_r_finMidB', 'DEF-f_middle.02.R'],
    ['def_r_finMidC', 'DEF-f_middle.03.R'],
    ['def_r_finThumbA', 'DEF-thumb.01.R'],
    ['def_r_finThumbB', 'DEF-thumb.02.R'],
    ['def_r_finThumbC', 'DEF-thumb.03.R'],
    ['def_r_finRingCarpal', 'def_r_finRingCarpal'], #Undefined in Rigify
    ['def_r_finRingA', 'DEF-f_ring.01.R'],
    ['def_r_finRingB', 'DEF-f_ring.02.R'],
    ['def_r_finRingC', 'DEF-f_ring.03.R'],
    ['def_r_finPinkyA', 'DEF-f_pinky.01.R'],
    ['def_r_finPinkyB', 'DEF-f_pinky.02.R'],
    ['def_r_finPinkyC', 'DEF-f_pinky.03.R'],
    ['def_r_thigh', 'DEF-thigh.R'],
    ['def_r_knee', 'DEF-shin.R'],
    ['def_r_kneeB', 'def_r_kneeB'],
    ['def_r_ankle', 'DEF-foot.R'],
    ['def_r_ball', 'DEF-toe.R'],
    #Center
    ['def_c_hip', 'DEF-spine'],
    ['def_c_spineA', 'DEF-spine.001'],
    ['def_c_spineB', 'DEF-spine.002'],
    ['def_c_spineC', 'DEF-spine.003'],
    ['def_c_neckA', 'DEF-spine.004'],
    ['def_c_neckB', 'DEF-spine.005'],
    ['def_c_head', 'DEF-spine.006'],
]


print("===New Run===")

obj= bpy.context.active_object

v = obj.vertex_groups

for n in weightList:
    if n[0] in v:
        v[n[0]].name = n[1]

print("===End Run===")