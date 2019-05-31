from chimerax.core.toolshed import BundleAPI

class _SeggerAPI(BundleAPI):

    @staticmethod
    def start_tool(session, tool_name):
        from .segment_dialog import Volume_Segmentation_Dialog
        d = Volume_Segmentation_Dialog.get_singleton(session, tool_name)
        return d

    @staticmethod
    def register_command(command_name, logger):
        # 'register_command' is lazily called when the command is referenced
        from . import segcmd
        segcmd.register_segger_command(logger)

bundle_api = _SeggerAPI()

# ------------------------------------------------------------------------------
#
dev_menus = False       # Include under-development menus.
timing = False          # Report execution times for optimizing code.
seggerVersion = '2.3'

from .regions import Segmentation, Region, SelectedRegions