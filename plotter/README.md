# Plotter Kernel

## Acknowldegements

This is where I started on learning how to create a simple kernel for Jupyter. 

This is a very nice article. 

Referring to the tutorial in the following source.

[Tutorial](https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781785888632/1/ch01lvl1sec16/creating-a-simple-kernel-for-jupyter)

## Plotter Kernel

This is a sample plotter kernel referring to the aforementioned
tutorial. The original tutorial holds all the codes and method to
write this kernel. This effort is mereley creating a streamlined 
workflow to use this and make it available for testing with an 
installation workflow. This includes installing the kernel code
and installing the jupyter kernel. 
 
I create a simple pip package to install this locally 
and make it accessible for general usage. A bug was also fixed
when releasing this code. 

The objective of this code snippets is 
to make available a workflow to create your plugin and install it
in the jupyter kernel space. 

## Installing

This is a mock model, so I placed it as a test pip package. 

```bash
pip install -i https://test.pypi.org/simple/ plotter-kernel-vibhatha==0.0.12 --user
```

This command will add the plotter kernel in your python user libs. 

Then install the kernel.

The kernel is located in the plotter1 folder. Install the kernel as follows;

```bash
jupyter kernelspec install --user plotter1
``` 

If you haven't installed jupyter and required packages, please do it first. 
Here I assume, y



#### Issue With Original Code

When running the original code, these exceptions are noted in the console where we
launched the command,

```bash
jupyter notebook
```

Here is the trace:

```bash
user:~/sandbox/temp$ jupyter notebook
[I 19:35:37.374 NotebookApp] [jupyter_nbextensions_configurator] enabled 0.4.1
[I 19:35:37.374 NotebookApp] Serving notebooks from local directory: /home/vibhatha/sandbox/temp
[I 19:35:37.374 NotebookApp] The Jupyter Notebook is running at:
[I 19:35:37.374 NotebookApp] http://localhost:8888/?token=705f220ba0eb0886ad6396eca4f3ca1cb8d0854ac7a297e8
[I 19:35:37.374 NotebookApp]  or http://127.0.0.1:8888/?token=705f220ba0eb0886ad6396eca4f3ca1cb8d0854ac7a297e8
[I 19:35:37.374 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 19:35:37.398 NotebookApp] 
    
    To access the notebook, open this file in a browser:
        file:///home/vibhatha/.local/share/jupyter/runtime/nbserver-17287-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/?token=705f220ba0eb0886ad6396eca4f3ca1cb8d0854ac7a297e8
     or http://127.0.0.1:8888/?token=705f220ba0eb0886ad6396eca4f3ca1cb8d0854ac7a297e8
[I 19:35:43.194 NotebookApp] Creating new notebook in 
[I 19:35:44.723 NotebookApp] Kernel started: 0ba89f4f-4e41-453f-8e24-ac03ef136ecb
[IPKernelApp] ERROR | Exception in message handler:
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 268, in dispatch_shell
    yield gen.maybe_future(handler(stream, idents, msg))
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 735, in run
    value = future.result()
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 209, in wrapper
    yielded = next(result)
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 541, in execute_request
    user_expressions, allow_stdin,
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 52, in do_execute
    y = f(x)
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 25, in <lambda>
    return lambda x: eval(code.split('=')[1].strip(),
IndexError: list index out of range
[IPKernelApp] ERROR | Exception in message handler:
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 268, in dispatch_shell
    yield gen.maybe_future(handler(stream, idents, msg))
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 735, in run
    value = future.result()
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 209, in wrapper
    yielded = next(result)
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 541, in execute_request
    user_expressions, allow_stdin,
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 52, in do_execute
    y = f(x)
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 25, in <lambda>
    return lambda x: eval(code.split('=')[1].strip(),
IndexError: list index out of range
[IPKernelApp] ERROR | Exception in message handler:
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 268, in dispatch_shell
    yield gen.maybe_future(handler(stream, idents, msg))
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 735, in run
    value = future.result()
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 209, in wrapper
    yielded = next(result)
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 541, in execute_request
    user_expressions, allow_stdin,
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 52, in do_execute
    y = f(x)
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 25, in <lambda>
    return lambda x: eval(code.split('=')[1].strip(),
IndexError: list index out of range
[IPKernelApp] ERROR | Exception in message handler:
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 268, in dispatch_shell
    yield gen.maybe_future(handler(stream, idents, msg))
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 735, in run
    value = future.result()
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 209, in wrapper
    yielded = next(result)
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 541, in execute_request
    user_expressions, allow_stdin,
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 52, in do_execute
    y = f(x)
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 25, in <lambda>
    return lambda x: eval(code.split('=')[1].strip(),
IndexError: list index out of range
[W 19:35:46.159 NotebookApp] 404 GET /static/components/codemirror/mode/plotter/plotter.js?v=20200111193537 (127.0.0.1) 8.97ms referer=http://localhost:8888/notebooks/Untitled2.ipynb?kernel_name=plotter1
[IPKernelApp] ERROR | Exception in message handler:
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 268, in dispatch_shell
    yield gen.maybe_future(handler(stream, idents, msg))
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 735, in run
    value = future.result()
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 209, in wrapper
    yielded = next(result)
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 541, in execute_request
    user_expressions, allow_stdin,
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 52, in do_execute
    y = f(x)
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 25, in <lambda>
    return lambda x: eval(code.split('=')[1].strip(),
IndexError: list index out of range
[IPKernelApp] ERROR | Exception in message handler:
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 268, in dispatch_shell
    yield gen.maybe_future(handler(stream, idents, msg))
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 735, in run
    value = future.result()
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 209, in wrapper
    yielded = next(result)
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 541, in execute_request
    user_expressions, allow_stdin,
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 52, in do_execute
    y = f(x)
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 25, in <lambda>
    return lambda x: eval(code.split('=')[1].strip(),
IndexError: list index out of range
[IPKernelApp] ERROR | Exception in message handler:
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 268, in dispatch_shell
    yield gen.maybe_future(handler(stream, idents, msg))
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 735, in run
    value = future.result()
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 209, in wrapper
    yielded = next(result)
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 541, in execute_request
    user_expressions, allow_stdin,
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 52, in do_execute
    y = f(x)
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 25, in <lambda>
    return lambda x: eval(code.split('=')[1].strip(),
IndexError: list index out of range
[IPKernelApp] ERROR | Exception in message handler:
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 268, in dispatch_shell
    yield gen.maybe_future(handler(stream, idents, msg))
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 735, in run
    value = future.result()
  File "/usr/local/lib/python3.7/dist-packages/tornado/gen.py", line 209, in wrapper
    yielded = next(result)
  File "/usr/local/lib/python3.7/dist-packages/ipykernel/kernelbase.py", line 541, in execute_request
    user_expressions, allow_stdin,
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 52, in do_execute
    y = f(x)
  File "/home/vibhatha/.local/lib/python3.7/site-packages/plotter_kernel/plotkernel.py", line 25, in <lambda>
    return lambda x: eval(code.split('=')[1].strip(),
IndexError: list index out of range

```

#### Fix 

This is not the perfect fix. But it will not show an exception in the console. 
There are better fixes for this. But I just used a simple exception handling method here.
Following code shows how the exception was handled.  

```python

def do_execute(self, code, silent,
               store_history=True,
               user_expressions=None,
               allow_stdin=False):

    # We create the plot with matplotlib.
    fig, ax = plt.subplots(1, 1, figsize=(6, 4),
                           dpi=100)
    plt.title(code)
    x = np.linspace(-5., 5., 200)

    if not code:
        return {'status': 'error',
                'execution_count':
                    self.execution_count,
                'payload': [],
                'user_expressions': {},
                }
    else:
        try:
            functions = code.split('\n')
            for fun in functions:
                f = _parse_function(fun)
                y = f(x)
                ax.plot(x, y)
            ax.set_xlim(-5, 5)

            # We create a PNG out of this plot.
            png = _to_png(fig)

            if not silent:
                # We send the standard output to the
                # client.
                self.send_response(
                    self.iopub_socket,
                    'stream', {
                        'name': 'stdout',
                        'data': ('Plotting {n} '
                                 'function(s)'). \
                            format(n=len(functions))})

                # We prepare the response with our rich
                # data (the plot).
                content = {
                    'source': 'kernel',

                    # This dictionary may contain
                    # different MIME representations of
                    # the output.
                    'data': {
                        'image/png': png
                    },

                    # We can specify the image size
                    # in the metadata field.
                    'metadata': {
                        'image/png': {
                            'width': 600,
                            'height': 400
                        }
                    }
                }

                # We send the display_data message with
                # the contents.
                self.send_response(self.iopub_socket,
                                   'display_data', content)

        except:
            return {'status': 'error',
                    'execution_count':
                        self.execution_count,
                    'payload': [],
                    'user_expressions': {},
                    }

        # We return the exection results.
    return {'status': 'ok',
            'execution_count':
                self.execution_count,
            'payload': [],
            'user_expressions': {},
            }


```

## Issues

Please create issues if you find bugs. If there are suggestions, please contribute by forking. 

## End Remarks

If you use this work, please credit the original authors. They have done an amazing work
in putting this as a very simple and clear tutorial. 
 
If our work is useful please credit us as well.

Happy Hacking!!!

## References

These are very useful resources that I used in learning writing Jupyter Kernels. 

1. [Jupyter Wrapper Kernels](https://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html)
2. [Bash Kernel](https://github.com/takluyver/bash_kernel)
3. [Echo Kernel](https://github.com/jupyter/echo_kernel) 
4. [Similar Source To Original Reference](https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781785888632/1/ch01lvl1sec16/creating-a-simple-kernel-for-jupyter)

