import logging
import maya.cmds as cmds

logging.basicConfig()
logger = logging.getLogger("mesh_resetter")
logger.setLevel(logging.INFO)

def reset_to_origin():
    selection = cmds.ls(selection=True)

    if not selection:
        cmds.warning('Nothing selected. Please select at least one object and try again.')
        return
    
    try:
        for obj in selection:
            cmds.move(0, 0, 0, obj, a=True, rpr=True)  
    except Exception as e:
        logger.debug(str(e))