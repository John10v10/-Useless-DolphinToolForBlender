from ctypes import *
from ctypes.wintypes import *

import bpy
import struct
from mathutils import Matrix

class DolphinFreeLookControlPanel(bpy.types.Panel):
    """Draws the UI panel for Dolphin's "Free Look" feature"""
    bl_label = "Dolphin Free Look Controls"
    bl_idname = "OBJECT_PT_dolphinfreelook"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        layout = self.layout

        layout.row().label(text="Access Code:")
        layout.row().prop(context.scene, "dolphin_free_look_matrix_access_code")
        layout.separator(factor=2)
        layout.row().prop(context.scene, "dolphin_free_look_strength")
        layout.row().prop(context.scene, "dolphin_free_look_strength_exponent")
        layout.row().operator("wm.start_consistent_matrix_sender_operator")
        layout.row().label(text="Press Q to quit going live.")

def writeToDolphin():

    fixYZ = Matrix(((1, 0, 0, 0),(0, 0, -1, 0),(0, 1, 0, 0),(0, 0, 0, 1)))
    
    if (bpy.context.scene.render.resolution_x > bpy.context.scene.render.resolution_y):
        aspect_matrix = Matrix(((1, 0, 0, 0),(0, bpy.context.scene.render.resolution_x/bpy.context.scene.render.resolution_y, 0, 0),(0, 0, 1, 0),(0, 0, 0, 1)))
    else:
        aspect_matrix = Matrix(((bpy.context.scene.render.resolution_y/bpy.context.scene.render.resolution_x, 0, 0, 0),(0, 1, 0, 0),(0, 0, 1, 0),(0, 0, 0, 1)))
    
    
    p = bpy.context.scene.camera.calc_matrix_camera(bpy.context.evaluated_depsgraph_get()) @ aspect_matrix
    
    if bpy.context.scene.camera.data.type == 'PERSP':
        p[2][2] = 0
        p[2][3] = -1
        p[3][2] = -1
    else:
        p[2][2] = -5.000250166631304e-05
        p[2][3] = -1.0000500679016113
        p[3][2] = 0.0

    mat = p @ bpy.context.scene.camera.matrix_world.inverted() @ fixYZ
    
    rot_mat = (bpy.context.scene.camera.matrix_world.inverted() @ fixYZ).to_3x3()

    mat_bytes = b''

    for r in mat:
        for c in r:
            mat_bytes += struct.pack("f", c)

    for r in rot_mat:
        for c in r:
            mat_bytes += struct.pack("f", c)
    
    mat_bytes += struct.pack("f", bpy.context.scene.dolphin_free_look_strength ** bpy.context.scene.dolphin_free_look_strength_exponent)

    OpenProcess = windll.kernel32.OpenProcess
    WriteProcessMemory = windll.kernel32.WriteProcessMemory
    CloseHandle = windll.kernel32.CloseHandle

    WriteProcessMemory.argtypes = [HANDLE,LPCVOID,LPVOID,c_size_t,POINTER(c_size_t)]

    PROCESS_ALL_ACCESS = 0x1F0FFF

    AccessCode = bpy.context.scene.dolphin_free_look_matrix_access_code

    pid = int(AccessCode[:8], 16)
    address = int(AccessCode[8:], 16)

    bufferSize = len(mat_bytes)
    buffer = c_char_p(mat_bytes)
    bytesWritten = c_ulonglong()

    processHandle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    WriteProcessMemory(processHandle, address, buffer, bufferSize, byref(bytesWritten))

    CloseHandle(processHandle)

class ConsistentMatrixSender(bpy.types.Operator):
    """Fires up the interval to consistently write to Dolphin's freelook matrix"""
    bl_idname = "wm.start_consistent_matrix_sender_operator"
    bl_label = "Go Live!"

    _timer = None

    @classmethod
    def poll(cls, context):
        return len(context.scene.dolphin_free_look_matrix_access_code) == 24

    def modal(self, context, event):
        if event.type in {'Q'}:
            self.cancel(context)
            return {'CANCELLED'}

        if event.type == 'TIMER':
            writeToDolphin()

        return {'PASS_THROUGH'}

    def execute(self, context):
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.1, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)


def register():
    bpy.utils.register_class(ConsistentMatrixSender)
    bpy.utils.register_class(DolphinFreeLookControlPanel)
    bpy.types.Scene.dolphin_free_look_matrix_access_code = bpy.props.StringProperty(name="")
    bpy.types.Scene.dolphin_free_look_strength = bpy.props.FloatProperty(name="Strength", default=1, min=0, max=1, subtype='FACTOR')
    bpy.types.Scene.dolphin_free_look_strength_exponent = bpy.props.FloatProperty(name="Strength Exponent", default=1, min=0)

def unregister():
    bpy.utils.unregister_class(ConsistentMatrixSender)


if __name__ == "__main__":
    register()