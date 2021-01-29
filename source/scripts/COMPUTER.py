from POST_BIOS import POST, BIOS
from CPU import kernel

Error = POST()
if Error is not None:
    print(Error)
else:
    BIOS(kernel)
