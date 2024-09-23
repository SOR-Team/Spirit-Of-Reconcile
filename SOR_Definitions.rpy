python:
    def sor_has_SuperuserPrivileges():
        """
        Tells if user running MAS has admin (Windows) or superuser/root (*nix)
        privileges.
        OUT:
            True - user has special privileges.
            False - user has no special privileges.
        """


        if renpy.windows:
            import ctypes

            try:
                return ctypes.windll.shell32.IsUserAnAdmin() == 1
            except AttributeError:
                return False

        else:
            import os

            try:
                return os.getuid() == 0
            except AttributeError:
                return False
