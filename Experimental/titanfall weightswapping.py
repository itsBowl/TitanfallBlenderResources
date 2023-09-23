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

#Weights undefined in rigify
#Bound to nearest match on rigify rig
retarget = [
    ['def_l_shoulderTwist', 'DEF-upper_arm.L'], 
    ['def_l_elbowB', 'def_l_elbowB'], #I am yet to find a model that uses this binding
    ['def_l_finRingCarpal', 'def_l_finRingCarpal'], #This requires reweighting the hand
    ['def_l_kneeB', 'DEF-thigh.L'],

    ['def_r_shoulderTwist', 'DEF-upper_arm.R'],
    ['def_r_elbowB', 'def_r_elbowB'],
    ['def_r_finRingCarpal', 'def_r_finRingCarpal'],
    ['def_r_kneeB', 'DEF-thigh.R'],

]

retarget = [
    ['def_l_shoulderTwist', 'def_l_shoulder'], 
    ['def_l_elbowB', 'def_l_elbowB'], #I am yet to find a model that uses this binding
    ['def_l_finRingCarpal', 'def_l_finRingCarpal'], #This requires reweighting the hand
    ['def_l_kneeB', 'def_l_knee'],

    ['def_r_shoulderTwist', 'def_r_shoulder'],
    ['def_r_elbowB', 'def_r_elbowB'],
    ['def_r_finRingCarpal', 'def_r_finRingCarpal'],
    ['def_r_kneeB', 'def_r_knee'],

]


print("===New Run===")

obj= bpy.context.active_object

v = obj.vertex_groups

#Rebinding to the rigify rig
for n in weightList:
    if n[0] in v:
        v[n[0]].name = n[1]

#Rebinding undefined in rigify weights to the rigify rig
i = 0
for n in retarget:
    for m in v:
        if m.name in n[0]:
            print("found " + m.name + " and " + n[0])
            for id, vert in enumerate(obj.data.vertices):
                available_groups = [v_group_elem.group for v_group_elem in vert.groups]
                A = B = 0
                if obj.vertex_groups[m.name].index in available_groups:
                    A = obj.vertex_groups[m.name].weight(id)
                if obj.vertex_groups[n[0]].index in available_groups:
                    B = obj.vertex_groups[n[0]].weight(id)

                # only add to vertex group is weight is > 0
                sum = A + B
                if sum > 0:
                    m.add([id], sum ,'REPLACE')




print("===End Run===")