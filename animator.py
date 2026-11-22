from maya import cmds
import random

def animate_selected_objects(window):

    selected_objects = cmds.ls(selection=True)
    cmds.cutKey(selected_objects, clear=True)

    for obj in selected_objects:

        for frame in range(0, window.duration_spinbox.value() + 1, window.step_spinbox.value()):
            
            cmds.setAttr(obj + ".translateX", random.uniform(window.minTX_spinbox.value(), window.maxTX_spinbox.value()))
            cmds.setAttr(obj + ".translateY", random.uniform(window.minTY_spinbox.value(), window.maxTY_spinbox.value()))
            cmds.setAttr(obj + ".translateZ", random.uniform(window.minTZ_spinbox.value(), window.maxTZ_spinbox.value()))

            cmds.setAttr(obj + ".rotateX", random.uniform(window.minRX_spinbox.value(), window.maxRX_spinbox.value()))
            cmds.setAttr(obj + ".rotateY", random.uniform(window.minRY_spinbox.value(), window.maxRY_spinbox.value()))
            cmds.setAttr(obj + ".rotateZ", random.uniform(window.minRZ_spinbox.value(), window.maxRZ_spinbox.value()))

            cmds.setAttr(obj + ".scaleX", random.uniform(window.minSX_spinbox.value(), window.maxSX_spinbox.value()))
            cmds.setAttr(obj + ".scaleY", random.uniform(window.minSY_spinbox.value(), window.maxSY_spinbox.value()))
            cmds.setAttr(obj + ".scaleZ", random.uniform(window.minSZ_spinbox.value(), window.maxSZ_spinbox.value()))

            cmds.setKeyframe(obj, time=frame)
            print("Frame:", frame)

