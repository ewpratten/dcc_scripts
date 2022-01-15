import logging
logger = logging.getLogger("eds.blender")
import bpy

# Modules
from eds.dcc.blender.modules.add_menu.pos_y_camera import ModuleAddYAlignedCamera
from eds.dcc.blender.modules.panels.camera_utils_panel import ModuleCameraUtils
from eds.dcc.blender.modules.operators.mouse_delta_rotation import ModuleOperatorMouseDeltaRotate

# List of independent modules to load
BLENDER_LOAD_MODULES = [
    ModuleAddYAlignedCamera,
    ModuleCameraUtils,
    ModuleOperatorMouseDeltaRotate
]


def register():
    logger.info("Registering Blender scripts")

    # Register all defined sub-modules
    for module in BLENDER_LOAD_MODULES:
        # Instantiate the module
        m = module()

        logger.info(f"Registering Blender sub-module: {m.get_name()}")
        m.register_blender_module()


def unregister():
    logger.info("Unregistering Blender scripts")

    # Unregister all defined sub-modules
    for module in BLENDER_LOAD_MODULES:
        # Instantiate the module
        m = module()

        logger.info(f"Unregistering Blender sub-module: {m.get_name()}")
        m.unregister_blender_module()


if __name__ == "__main__":
    logging.info("Started via `__main__`")
    register()