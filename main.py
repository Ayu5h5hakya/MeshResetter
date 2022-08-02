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
    errors = ''
    try:
        for obj in selection:
            try:
                cmds.move(0, 0, 0, obj, a=True, rpr=True)  
            except Exception as e:
                errors += str(e) + '\n'
        if errors != '':
            print('ERROR!')
            print(errors)
    except Exception as e:
        logger.debug(str(e))