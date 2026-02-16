# Knows Issues

## No Microsoft Visual C++ 14.0 or greater (Windows)

Terminal Output:
```
Building wheels for collected packages: roboticstoolbox-python, rtb-data
  Building wheel for roboticstoolbox-python (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for roboticstoolbox-python (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [2563 lines of output]

(panjang pokoknya)

      running build_ext
      building 'roboticstoolbox.frne' extension
      error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for roboticstoolbox-python
  Building wheel for rtb-data (pyproject.toml) ... done
  Created wheel for rtb-data: filename=rtb_data-1.0.1-py3-none-any.whl size=115135990 sha256=01da83979dc860ee486ebd09dbd58fb7b61e2ad647d588489d4a7659f205a371
  Stored in directory: C:\Users\Gemilang\AppData\Local\Temp\pip-ephem-wheel-cache-fhir3__d\wheels\f1\be\48\3b075c2c026666f5263df04c8f1dfc8bf5977bc72e8a25cd5f
Successfully built rtb-data
Failed to build roboticstoolbox-python
error: failed-wheel-build-for-install

× Failed to build installable wheels for some pyproject.toml based projects
╰─> roboticstoolbox-python
```

Solutions:

1. Go to [this link](https://visualstudio.microsoft.com/visual-cpp-build-tools/) and click "Download Build Tools".
2. Install the build tools. It should appears as "Visual Studio Installer"
3. Open, click "Modify", and look for "Desktop development with C++
4. Make sure "MSVC v143 - VS 2022 ..." and "Windows 11 SDK ..." checked, and proceed to install.
5. Retry installing the Robotics Toolbox for Python by invoking `pip cache purge` in the activated virtual environment and invoke `pip3 install rvc3python` after that.

## Numpy error

Terminal output:
```
A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.4.2 as it may crash. To support both 1.x and 2.x
versions of NumPy, modules must be compiled with NumPy 2.0.
Some module may need to rebuild instead e.g. with 'pybind11>=2.12'.

If you are a user of the module, the easiest solution will be to
downgrade to 'numpy<2' or try to upgrade the affected module.
We expect that some modules will need time to support NumPy 2.

Traceback (most recent call last):  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\ipykernel_launcher.py", line 18, in <module>
    app.launch_new_instance()
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\traitlets\config\application.py", line 1075, in launch_instance
    app.start()
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\ipykernel\kernelapp.py", line 758, in start
    self.io_loop.start()
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\tornado\platform\asyncio.py", line 211, in start
    self.asyncio_loop.run_forever()
  File "C:\Users\Gemilang\AppData\Local\Python\pythoncore-3.11-64\Lib\asyncio\base_events.py", line 608, in run_forever
    self._run_once()
  File "C:\Users\Gemilang\AppData\Local\Python\pythoncore-3.11-64\Lib\asyncio\base_events.py", line 1936, in _run_once
    handle._run()
  File "C:\Users\Gemilang\AppData\Local\Python\pythoncore-3.11-64\Lib\asyncio\events.py", line 84, in _run
    self._context.run(self._callback, *self._args)
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\ipykernel\kernelbase.py", line 621, in shell_main
    await self.dispatch_shell(msg, subshell_id=subshell_id)
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\ipykernel\kernelbase.py", line 478, in dispatch_shell
    await result
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\ipykernel\ipkernel.py", line 372, in execute_request
    await super().execute_request(stream, ident, parent)
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\ipykernel\kernelbase.py", line 834, in execute_request
    reply_content = await reply_content
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\ipykernel\ipkernel.py", line 464, in do_execute
    res = shell.run_cell(
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\ipykernel\zmqshell.py", line 663, in run_cell
    return super().run_cell(*args, **kwargs)
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\IPython\core\interactiveshell.py", line 3123, in run_cell
    result = self._run_cell(
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\IPython\core\interactiveshell.py", line 3178, in _run_cell
    result = runner(coro)
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\IPython\core\async_helpers.py", line 128, in _pseudo_sync_runner
    coro.send(None)
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\IPython\core\interactiveshell.py", line 3400, in run_cell_async
    has_raised = await self.run_ast_nodes(code_ast.body, cell_name,
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\IPython\core\interactiveshell.py", line 3641, in run_ast_nodes
    if await self.run_code(code, result, async_=asy):
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\IPython\core\interactiveshell.py", line 3701, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "C:\Users\Gemilang\AppData\Local\Temp\ipykernel_23440\3100500685.py", line 2, in <module>
    import roboticstoolbox as rtb
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\roboticstoolbox\__init__.py", line 1, in <module>
    from roboticstoolbox.tools import *
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\roboticstoolbox\tools\__init__.py", line 2, in <module>
    from roboticstoolbox.tools.p_servo import p_servo, angle_axis, angle_axis_python
  File "C:\Users\Users\User\temp\.venv\Lib\site-packages\roboticstoolbox\tools\p_servo.py", line 7, in <module>
    from roboticstoolbox.fknm import Angle_Axis
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
AttributeError: _ARRAY_API not found
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
Cell In[1], line 2
      1 # Try this example within a Jupyter Notebook Cell!
----> 2 import roboticstoolbox as rtb
      3 import spatialmath as sm
      4 import numpy as np

File ~\temp\.venv\Lib\site-packages\roboticstoolbox\__init__.py:1
----> 1 from roboticstoolbox.tools import *
      3 from roboticstoolbox.robot import *
      5 from roboticstoolbox.mobile import *

File ~\temp\.venv\Lib\site-packages\roboticstoolbox\tools\__init__.py:2
      1 from roboticstoolbox.tools.null import null
----> 2 from roboticstoolbox.tools.p_servo import p_servo, angle_axis, angle_axis_python
      3 from roboticstoolbox.tools.Ticker import Ticker
      4 from roboticstoolbox.tools.urdf import *  # noqa

File ~\temp\.venv\Lib\site-packages\roboticstoolbox\tools\p_servo.py:7
      5 import math
      6 from typing import Union
----> 7 from roboticstoolbox.fknm import Angle_Axis
      9 ArrayLike = Union[list, np.ndarray, tuple, set]
     12 def angle_axis(T, Td):

ImportError: numpy.core.multiarray failed to import
```

Solution:

1. Uninstall `numpy` by invoking `pip uninstall numpy` and `pip cache purge` in an activated virtual environment.
2. Install `numpy` again by invoking `pip install numpy==1.26.4` [like this](https://github.com/petercorke/robotics-toolbox-python/issues/454).