from maya import cmds
import random

def animate_selected_objects(window): # animates selected objects based on the parameters set in the UI

    selected_objects = cmds.ls(selection=True) # only applies to selected objects
    cmds.cutKey(selected_objects, clear=True) # clears any existing keyframes on the selected objects (before making new animation)

    cmds.undoInfo(openChunk=True, chunkName="Selection Animation") # opens an undo chunk so that the entire animation can be undone in one step
    try:
        for obj in selected_objects:

            for frame in range(0, window.duration_spinbox.value() + 1, window.step_spinbox.value()): # creates a key for each frame based on step value

                # Sets random translation values based on min and max
                cmds.setAttr(obj + ".translateX", random.uniform(window.minTX_spinbox.value(), window.maxTX_spinbox.value()))
                cmds.setAttr(obj + ".translateY", random.uniform(window.minTY_spinbox.value(), window.maxTY_spinbox.value()))
                cmds.setAttr(obj + ".translateZ", random.uniform(window.minTZ_spinbox.value(), window.maxTZ_spinbox.value()))

                # Sets random rotation values based on min and max
                cmds.setAttr(obj + ".rotateX", random.uniform(window.minRX_spinbox.value(), window.maxRX_spinbox.value()))
                cmds.setAttr(obj + ".rotateY", random.uniform(window.minRY_spinbox.value(), window.maxRY_spinbox.value()))
                cmds.setAttr(obj + ".rotateZ", random.uniform(window.minRZ_spinbox.value(), window.maxRZ_spinbox.value()))

                # Sets random scale values based on min and max
                cmds.setAttr(obj + ".scaleX", random.uniform(window.minSX_spinbox.value(), window.maxSX_spinbox.value()))
                cmds.setAttr(obj + ".scaleY", random.uniform(window.minSY_spinbox.value(), window.maxSY_spinbox.value()))
                cmds.setAttr(obj + ".scaleZ", random.uniform(window.minSZ_spinbox.value(), window.maxSZ_spinbox.value()))

                cmds.setKeyframe(obj, time=frame) # sets a keyframe for the selected object
    finally:
        cmds.undoInfo(closeChunk=True) # closes the undo chunk
