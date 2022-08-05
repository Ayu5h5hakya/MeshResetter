import logging
import maya.cmds as cmds
import sys

logging.basicConfig()
logger = logging.getLogger("mesh_resetter")
logger.setLevel(logging.INFO)

def reset_to_origin():
    selection = cmds.ls(selection=True)

    if not selection:
        cmds.warning('Nothing selected. Please select at least one object and try again.')
        return
    counter = 0
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

        if counter > 0:
            pivot_pos = 'origin'
            is_plural = 'objects were'
            affected = str(counter)
            if counter == 1:
                is_plural = ' was'
            message = affected + ' ' + is_plural + ' moved to the ' + pivot_pos
            sys.stdout.write(message)
    except Exception as e:
        logger.debug(str(e))