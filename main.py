import logging

logging.basicConfig()
logger = logging.getLogger("mesh_resetter")
logger.setLevel(logging.INFO)

def reset_to_origin():
    selection = cmds.ls(selection=True)
    selection_short = cmds.ls(selection=True)

    if not selection:
        cmds.warning('Nothing selected. Please select at least one object and try again.')
        return