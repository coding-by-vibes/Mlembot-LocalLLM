# The KoboldCpp FAQ and Knowledgebase
[**NEED A GGUF MODEL? CLICK HERE AND READ!**](https://github.com/LostRuins/koboldcpp/wiki#what-models-does-koboldcpp-support-what-architectures-are-supported)  
Welcome to the KoboldCpp knowledgebase! If you have issues with KoboldCpp, please check if your question is answered here or in one of the link reference first. If not, you can open an issue on Github, or contact us on our [KoboldAI Discord Server](https://koboldai.org/discord). You can find me there as Mlembot, or just ask around (we have plenty of people around to help).

## Introduction
### **What is KoboldCpp?**  
KoboldCpp is an easy-to-use AI text-generation software for GGML and GGUF models, inspired by the original KoboldAI. It's a single self-contained distributable from Mlembot, that builds off llama.cpp, and adds a versatile **KoboldAI API endpoint**, additional format support, Stable Diffusion image generation, speech-to-text, backward compatibility, as well as a fancy UI with persistent stories, editing tools, save formats, memory, world info, author's note, characters, scenarios and everything KoboldAI and KoboldAI Lite have to offer.

## Getting an AI model file
### **What models does KoboldCpp support? What architectures are supported?**  
Generally, **all up-to-date GGUF models are supported**, and KoboldCpp also includes backward compatibility for older versions/legacy GGML `.bin` models, though some newer features might be unavailable.
- An incomplete list of architectures is listed, but there are *many hundreds of other GGUF models*. In general, if it's GGUF, it should work.
  - Llama / Llama2 / Llama3 / Alpaca / GPT4All / Vicuna / Koala / Pygmalion / Metharme / WizardLM / Mistral / Mixtral / Miqu / Qwen / Qwen2 / Yi / Gemma / Gemma2 / GPT-2 / Cerebras / Phi-2 / Phi-3 / GPT-NeoX / Pythia / StableLM / Dolly / RedPajama / GPT-J / RWKV4 / MPT / Falcon / Starcoder / Deepseek and many, **many** more.
- The best place to get GGUF text models is **Huggingface**. For image models, **CivitAI** has a good selection. Here are some to get you started.
  - A quick and easy text model to start with is [Airoboros Mistral 7B](https://huggingface.co/TheBloke/airoboros-mistral2.2-7B-GGUF/resolve/main/airoboros-mistral2.2-7b.Q4_K_S.gguf) (smaller and weaker) or [Tiefighter 13B](https://huggingface.co/KoboldAI/LLaMA2-13B-Tiefighter-GGUF/resolve/main/LLaMA2-13B-Tiefighter.Q4_K_S.gguf) (larger model) or [Beepo 22B](https://huggingface.co/mlembot/Beepo-22B-GGUF/resolve/main/Beepo-22B-Q4_K_S.gguf) (largest and most powerful).
  - Other good text generation models to try are [L3-8B-Stheno-v3.2](https://huggingface.co/bartowski/L3-8B-Stheno-v3.2-GGUF/resolve/main/L3-8B-Stheno-v3.2-Q4_K_S.gguf) and [Fimbulvetr-11B-v2](https://huggingface.co/mradermacher/Fimbulvetr-11B-v2-GGUF/resolve/main/Fimbulvetr-11B-v2.Q4_K_S.gguf)
  - Image Generation: [Anything v3](https://huggingface.co/admruul/anything-v3.0/resolve/main/Anything-V3.0-pruned-fp16.safetensors) or [Deliberate V2](https://huggingface.co/Yntec/Deliberate2/resolve/main/Deliberate_v2.safetensors) or [Dreamshaper SDXL](https://huggingface.co/Lykon/dreamshaper-xl-v2-turbo/resolve/main/DreamShaperXL_Turbo_v2_1.safetensors)
  - Image Recognition MMproj: [Pick the correct one for your model architecture here](https://huggingface.co/koboldcpp/mmproj/tree/main)
  - Speech Recognition: [Whisper models for Speech-To-Text](https://huggingface.co/koboldcpp/whisper/tree/main)
  - Text-To-Speech: [TTS models for Narration](https://huggingface.co/koboldcpp/tts/tree/main)
  - This is just a list for noobs to get started! There are hundreds more GGUFs out there!

Other formats such as safetensors and pytorch.bin models are not natively supported, and must be converted to GGUF/GGML! (see below)  

### **Where can I find or download GGUF and GGML models for KoboldCpp?**  
- GGML models can be found uploaded on [Huggingface](https://huggingface.co/models), simply by searching for `GGML` or `GGUF`. They should be a file in `.bin` or `.gguf` format
- A large selection of high quality models can also be found on [TheBloke's Huggingface Repo](https://huggingface.co/TheBloke), look for GGUF/GGML. 
- Lastly, you can also convert the models yourself, using the [appropriate quantization and conversion tools](https://kcpptools.mlembot.workers.dev). 

### **What's the difference between GGUF and GGML formats**  
GGUF is a newer format designed to (hopefully) be more future proof. As of Oct 2023, it is the latest and recommended format for LLAMA and LLAMA2 models. For other architectures, the old format is still used. KoboldCpp remains compatible with any version of both formats.

### **What are the differences between the different files for each model? Do I need them all? Which Quantization? F16? Q4_0? Q5_1?**  
No, you don't need all the files, just a single one. Each GGML model is just a single .bin or .gguf file. The multiple files represent different compression levels of each model, from worst to best (least to most bits-per-weight) in ascending order. A Q4_0 of a specific model will be smaller than a Q5_1, but of slightly lower quality. [Read more here](https://www.reddit.com/r/LocalLLaMA/comments/13l0j7m/a_comparative_look_at_ggml_quantization_and/).
- In general the quality (from worst to best) and filesize (from smallest to biggest) follows this order: 
- Q2K, Q3_K_S, Q3_K_M, Q3_K_L, Q4_0, Q4_K_S, Q4_1, Q4_K_M, Q5_0, Q5_1, Q5_K_S, Q5_K_M, Q6_K, Q8_0, F16

## Quick Start
### **How do I get started with KoboldCpp? What do I need? How do I compile KoboldCpp from source code?**  
This depends on the platform you are using, and what capabilities you want to use. First, **obtain and download a GGUF model file as stated above**. Next: 
- Windows, Using Prebuilt Executable (Easiest):  
  - [Download the latest koboldcpp.exe release here](https://github.com/LostRuins/koboldcpp/releases/latest)
  - Double click KoboldCPP.exe and select model OR run "KoboldCPP.exe --help" in CMD prompt to get command line arguments for more control.
  - Generally you don't have to change much besides the `Presets` and `GPU Layers`. Run with CuBLAS or CLBlast for GPU acceleration.
  - Select your GGUF or GGML model you downloaded earlier, and connect to the displayed URL once it finishes loading. 

- Linux, Precompiled Binary or AutoInstall script (Easy):  
  - On Linux, we provide a `koboldcpp-linux-x64-cuda1150` PyInstaller prebuilt binary on the **[releases](https://github.com/LostRuins/koboldcpp/releases/latest)** page for modern systems. Simply download and run the binary (You may have to `chmod +x` it first).  
  - Alternatively, you can also install koboldcpp to the current directory by running the following terminal command: `curl -fLo koboldcpp https://github.com/LostRuins/koboldcpp/releases/latest/download/koboldcpp-linux-x64 && chmod +x koboldcpp`. 
  - When you can't use the precompiled binary directly, we provide an automated build script which uses conda to obtain all dependencies, and generates (from source) a ready-to-use a pyinstaller binary for linux users. Simply execute the build script with `./koboldcpp.sh dist` and run the generated binary.

- MacOS (Precompiled Binary)
  - PyInstaller binaries for Modern ARM64 MacOS (M1, M2, M3) are now available! **[Simply download the MacOS binary](https://github.com/LostRuins/koboldcpp/releases/latest)**
  - In a MacOS terminal window, set the file to executable with `chmod +x koboldcpp-mac-arm64` and run it with `./koboldcpp-mac-arm64`.
  - In newer MacOS you may also have to whitelist it in security settings if it's blocked. [Here's a video guide](https://youtube.com/watch?v=NOW5dyA_JgY).

- MacOS and Linux (Self Compile):  
  - To compile your binaries from source, clone the repo with `git clone https://github.com/LostRuins/koboldcpp.git`
  - A makefile is provided, simply run `make`.
  - Optional Vulkan: Link your own install of Vulkan SDK manually with `make LLAMA_VULKAN=1`
  - Optional CLBlast: Link your own install of CLBlast manually with `make LLAMA_CLBLAST=1`
  - Note: for these you will need to obtain and link OpenCL and CLBlast libraries.
    - For Arch Linux: Install `cblas` and `clblast`.
    - For Debian: Install `libclblast-dev`.
  - You can attempt a CuBLAS build with `make LLAMA_CUBLAS=1` or using the provided CMake file, you will need CUDA toolkit installed.
  - For a full featured build, do `make LLAMA_VULKAN=1 LLAMA_CLBLAST=1 LLAMA_CUBLAS=1`
  - After all binaries are built, you can run the python script with the command `koboldcpp.py [ggml_model.gguf] [port]`
- MacOS Notes:
  - You may want to compile with `make LLAMA_METAL=1`, and enable it afterwards by passing --gpulayers (number)
  
- Windows, Compiling from Source Code:  
  - You're encouraged to use the .exe released, but if you want to compile your binaries from source at Windows, the easiest way is:
    - Get the latest release of w64devkit (https://github.com/skeeto/w64devkit). Be sure to use the "vanilla one", not i686 or other different stuff. If you try they will conflit with the precompiled libs!
    - Clone the repo with `git clone https://github.com/LostRuins/koboldcpp.git`
    - Make sure you are using the w64devkit integrated terminal, then run `make` at the KoboldCpp source folder. This will create the .dll files.
    - If you want to generate the .exe file, make sure you have the python module PyInstaller installed with pip (`pip install PyInstaller`). Then run the script `make_pyinstaller.bat`
    - The koboldcpp.exe file will be at your dist folder.
  - **Building with CUDA**: Visual Studio, CMake and CUDA Toolkit is required. Clone the repo, then open the CMake file and compile it in Visual Studio. Copy the `koboldcpp_cublas.dll` generated into the same directory as the `koboldcpp.py` file. If you are bundling executables, you may need to include CUDA dynamic libraries (such as `cublasLt64_11.dll` and `cublas64_11.dll`) in order for the executable to work correctly on a different PC.
  - **Replacing Libraries (Not Recommended)**: If you wish to use your own version of the additional Windows libraries (OpenCL, CLBlast, Vulkan), you can do it with:
    - OpenCL - tested with https://github.com/KhronosGroup/OpenCL-SDK . If you wish to compile it, follow the repository instructions. You will need vcpkg.
    - CLBlast - tested with https://github.com/CNugteren/CLBlast . If you wish to compile it you will need to reference the OpenCL files. It will only generate the ".lib" file if you compile using MSVC.
    - Move the respectives .lib files to the /lib folder of your project, overwriting the older files.
    - Also, replace the existing versions of the corresponding .dll files located in the project directory root (e.g. clblast.dll).
    - Make the KoboldCpp project using the instructions above.
  
- Android: 
  - Please refer to the "Installing KoboldCpp on Android via Termux" guide below.
  
- WSL:
  - You could, but why would you want to? The basic `make` should work without issues with build essentials. Finding appropriate libraries for GPU acceleration may be difficult.
 
## KoboldCpp General Usage and Troubleshooting  
### **I don't want to use the GUI launcher. How to use the 'command line/terminal' with extra parameters to launch koboldcpp?**  
Here are some easy ways to start koboldcpp from the command line. Pick one that suits you best.  
- Windows: Go to Start > Run (or WinKey+R) and input the full path of your koboldcpp.exe followed by the launch flags. e.g. `C:\mystuff\koboldcpp.exe --usecublas --gpulayers 10`. Alternatively, you can also create a desktop shortcut to the koboldcpp.exe file, and set the desired values in the `Properties > Target` box. Lastly, you can also start command prompt in your koboldcpp.exe directory (with `cmd`), and pass the desired flags to it from the terminal window.  
- Linux/OSX: Navigate to the koboldcpp directory, and build koboldcpp with `make` (as described in 'How do I compile KoboldCpp'). Then run the command `python3 koboldcpp.py --model (path you your model)`, plus whatever flags you need e.g. `--useclblast` or `--stream`

### **How do I see the available commands and how to use them?**  
You can launch KoboldCpp from the command line with the `--help` parameter to view the available command list. See the section on "How to use the command line terminal"

### **How much RAM/VRAM do I need to run Koboldcpp? What about my GPU?**  
The amount of RAM required depends on multiple factors such as the context size, quantization type, and parameter count of the model. In general, assuming a 2048 context with a Q4_0 quantization:
- LLAMA 3B needs at least 4GB RAM
- LLAMA 7B needs at least 8GB RAM
- LLAMA 13B needs at least 16GB RAM
- LLAMA 30B needs at least 32GB RAM
- LLAMA 65B needs at least 64GB RAM  

Offloading layers to the GPU VRAM can help reduce RAM requirements, while a larger context size or larger quantization can increase RAM requirements.
For number of layers to offload, see the section on GPU layer offloading.

### **What does GPU layer offloading do? How many layers can I offload?**  
Just running with `--usecublas` or `--useclblast` or `--usevulkan` will perform prompt processing on the GPU, but combined with GPU offloading via `--gpulayers` takes it one step further by offloading individual layers to run on the GPU, for per-token inference as well, greatly speeding up inference. The number of layers you can offload to GPU vram depends on many factors, some of which are already mentioned above, and can also change depending on which backend (CUDA/CL/Metal) that you are using. For reference, at 2048 context in Q4_0, a 6GB Nvidia RTX 2060 can comfortably offload:
- 32 layers with LLAMA 7B
- 18 layers with LLAMA 13B
- 8 layers with LLAMA 30B
You can specify `--gpulayers -1` and allow KoboldCpp to guess how many layers it should offload, though this is often not the most accurate, and doesn't work accurately for multi-gpu setups. You are recommended to determine the optimal layer fit through trial and error for best results.

### **How can I run KoboldCpp on my android phone (Termux)?**  
Inference directly on a mobile device is probably not optimal as it's likely to be slow and memory limited. Consider running it remotely instead, as described in the "Running remotely over network" section. If you still want to proceed, the best way on Android is to build and run KoboldCpp within Termux. Also, check out the guide below "Installing KoboldCpp on Android via Termux".

- [Install and run Termux from F-Droid](https://f-droid.org/en/packages/com.termux/)
- Enter the command `termux-change-repo` and choose `Mirror by BFSU`
- Install dependencies with `pkg install wget git python` (plus any other missing packages)
- Install dependencies `apt install openssl` (if needed)
- Clone the repo `git clone https://github.com/LostRuins/koboldcpp.git`
- Navigate to the koboldcpp folder `cd koboldcpp`
- Build the project `make`
- Grab a small GGUF model, such as `wget https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q2_K.gguf`
- Start the python server `python koboldcpp.py --model phi-2.Q2_K.gguf`
- Connect to `http://localhost:5001` on your mobile browser
- If you encounter any errors, make sure your packages are up-to-date with `pkg up`

### **What are my options to make it go FASTER? (CuBLAS/CLblast/Metal/Accelerate/ROCm/Vulkan)**  
By default, launching with no parameters set will attempt to pick the best backend available, but this can be optimized.  
Here are some options to Make It Fast:  
- CuBLAS: Only for Nvidia GPUs. Launch with `--usecublas` to use this. Prepackaged for windows .exe users, but requires installing CUDA toolkit for all other platforms (see compiling with CUDA from source, OSX/Mac section). Can be combined together with `--gpulayers` for even faster GPU offloading.
- CLblast: For most GPUs, including Nvidia, AMD, and Intel iGPUs. Launch with `--useclblast [platformID] [deviceID]` to use this. Prepackaged for windows .exe users, but requires installing CLBlast library for all other platforms (see compiling with CLBlast from source, OSX/Mac section). Can be combined together with `--gpulayers` for even faster GPU offloading.
- Metal: Only for Apple Silicon users (eg. Mac M2), GPU acceleration with Metal. Can be combined together with `--gpulayers`. See compiling with Metal from source.
- Accelerate: Only for mac users, CPU only. Automatically supported if you build on a mac. If BLAS is slowing you down, try `--noblas`.
- ROCm: Not directly supported, but see [YellowRoseCx/koboldcpp-rocm](https://github.com/YellowRoseCx/koboldcpp-rocm) fork via HIPBLAS for AMD devices only. Alternatively, try the Vulkan option.
- Vulkan: For most users, you can get very decent speeds by selecting the **Vulkan** option instead, which supports both Nvidia and AMD GPUs. Vulkan is a newer option that provides a good balance of speed and utility compared to the OpenCL backend.
- OpenBLAS (Removed): OpenBLAS was a BLAS acceleration library formerly used for prompt processing on the CPU. It has been deprecated and is no longer available. Instead, just use `--usecpu` to automatically launch in CPU mode, everything is handled automatically.

### **What values do I put for the `--useclblast [platform] [device]` command?**  
The two values to use represent the Platform ID and Device ID of your target GPU. For most systems, it will be 0 and 0 for the default GPU, e.g. `--useclblast 0 0`, but if you have more than 1 GPU, you can also try `--useclblast 1 0` and `--useclblast 0 1` with trial and error (it will print out the name of each selected device). When launching with CLBlast, the list of available GPUs and their IDs will then be printed in sequence to the terminal, which you can use as a reference. Also, another way to get the actual value to use is with the command line program `clinfo`, which will display the platform and device IDs for all your GPUs.

### **How do I run KoboldCpp on a different device than my PC over the network? Remote play?**  
There are multiple ways to use KoboldCpp on a different device over the network.  
1. If on a different LAN (Windows or Linux) - Use a Cloudflared tunnel. After launching KoboldCpp with default port 5001, run the `Remote-Link.cmd` included in the repo, which will create a cloudflared tunnel. Then just open your mobile browser to the displayed trycloudflare URL. In newer versions of KoboldCpp, there's a helper command to do all that for you, simply use `--remotetunnel` and it will proceed to setup a tunnel with a usable URL.
2. If on a different LAN (Any, Public) - Use the AI Horde. KoboldCpp comes with an embedded AI Horde worker (see section on Horde). You can start a worker, and then connect to it via the web version of Kobold Lite at https://lite.koboldai.net
3. If on same LAN - If you're on the same Wifi network, you can probably connect over LAN by navigating to the local IP of the host device (the PC running koboldcpp). For example, http://192.168.1.85:5001 or similar, check your LAN IP address. If that fails, try using the `--host` option with your LAN IP. If you setup port forwarding to a public IP, then it will be accessible over the internet as well.
4. There is a [Colab Notebook](https://github.com/LostRuins/koboldcpp/blob/mlembot/colab.ipynb) included here. It should work out of the box. use it at your own risk.

### **What port does Koboldcpp use? How do I change the port that koboldcpp uses?**  
By default KoboldCpp uses port 5001, but this can be changed with the `--port` launch parameter. You would connect your browser locally to that port for the UI or API, in the format http://localhost:port (e.g. http://localhost:5001). If the connection does not work, check your wifi or firewall settings, or try using a different port.

### **How do I use streaming? What are the types of streaming supported?**  
KoboldCpp now supports a variety of streaming options. Kobold Lite UI supports streaming out of the box, which can be toggled in Kobold Lite settings.  _Note: the `--stream` parameter is now deprecated and should not be used._ 
- Polled-Streaming (Recommended): This is the default used by the Kobold Lite UI. It polls for updates on the `/api/extra/generate/check` endpoint every second. It is relatively fast and simple to use, although some may find it a bit "chunky" as it does not update instantaneously every single token.
- Pseudo-Streaming: This is an older method that is no longer recommended, due to performance overheads. To use it with Kobold Lite, enable streaming, then append a `&streamamount=x` at the end of the Lite URL where X is the number of tokens per request. Negative performance impact.
- SSE (True Streaming): This type of streaming is only supported by a few third party clients such as SillyTavern and Agnaistic, available only via the API. It provides instantaneous per-token updates, but requires a persistent connection and some special handling on the client side with SSE support. This mode is not used in Lite or the main KoboldAI client. It uses a different API endpoint, so configure this from your third party client according to their provided instructions.

### **How to choose how many threads to use? What about `--blasthreads`?**  
Set number of threads to be used for inference. The optimal number of threads to use is usually approximately equal to the number of physical CPU cores your system has. So a i7-9750H with 12 logical processors and 6 physical cores would do best with either 5 or 6 threads. Setting `--blasthreads` will use a different number of threads during BLAS if specified. Otherwise, has the same value as `--threads`. Tf you leave the parameter blank, it will be set to a good default also based on slightly less than your CPU count. If running with full GPU offload, then setting 1 thread may be enough.  
_Note: The flag `psutil_set_threads` has been deprecated and should not be used._

### **What is BLAS? What is blasbatchsize? How does it affect me?**  
BLAS (Basic Linear Algebra Subprograms) is what is used to perform large matrix to matrix multiplication, which is needed for accelerated prompt processing. There are multiple backends this can be done with, such as CuBLAS(Nvidia), CLBlast(OpenCL), or Vulkan(AMD and Nvidia). The `--blasbatchsize` indicates the number of tokens in a single batch to be processed at once. Usually, you do not need to change this value (defaults to 512 for llama and 256 otherwise), but you can try lower values such as 128 for devices with less memory, at the expense of lower prompt processing speeds. BLAS is not used during stochastic sampling (generation).

### **What is Mirostat? How do I use it?**  
Mirostat is a newer sampling method that adjusts the value of k in top-k decoding to keep the perplexity within a specific range. In this way, it avoids two common problems in text generation: the boredom trap, in which the generated text becomes repetitive, and the perplexity trap, in which the generated text loses coherence. It can be used as a replacement for more classic samplers like Top-P, if enabled it replaces your samplers with mirostat. Takes 3 parameters = [type(0/1/2), tau(5.0), eta(0.1)]. Mirostat can now also be set on a per-generation basis within the API.  
_Note: the `--usemirostat` launch parameter has been deprecated and should not be used._

### **What is Grammar Sampling**  
Grammar Sampling allows you to specify a GBNF grammar format to be used when generating, constraining the AI to a specific syntax in the response. For more info, check out [this link](https://github.com/ggerganov/llama.cpp/pull/1773).

### **What is `--nomodel`**  
This parameter launches the KoboldAI Lite UI alone without loading a model. The Kobold Lite UI can be used to connect to an external KoboldCpp instance, or other AI services such as the AI Horde.

### **What is `--config`? What are .kcpps files?**  
`.kcpps` files are configuration files that store your KoboldCpp launcher preferences and settings. You can save and load them into the GUI, or run them directly with the `--config` flag.

### **What are .kcppt files?**  
`.kcppt` files are configuration *templates* that store KoboldCpp launcher preferences and settings. You can save and load them into the GUI, or run them directly with the `--config` flag. The difference between this and .kcpps files is that .kcppt files are intended to be shared, thus they will not include device specific settings like the GPU to use, instead those are decided by the other user.

### **What is `--multiuser` mode?**  
Multiuser mode allows multiple people to share a single KoboldCpp instance, connecting different devices to a common endpoint (over LAN, a port forwarded public IP, or through an internet tunnel). It's enabled by default. It automatically handles queuing requests and dispatching them to the correct clients. An optional extra parameter number allows you to specify the max simultaneous users. Set to `--multiuser 0` to disable this.

### **What is `--foreground`**  
This parameter is intended for window users. It sends the console terminal to the foreground every time a new prompt is generated, to avoid some idling slowdown issues.

### **What is `--quiet`**  
This parameter prevents prompt and generation output information from being displayed on the terminal. Useful for added privacy.

### **What is `--unpack`**  
Launching with this flag allows the internal contents of the KoboldCpp pyinstaller binary to be unpacked into a directory. This is useful for modifying or replacing files, and KoboldCpp can then be launched by running `python3 koboldcpp.py`

### **What is `--showgui`**  
Adding the `--showgui` flag allows the GUI to be shown even with command line flags are used. Instead, command line flags will get imported into the GUI itself, allowing them to be modified. This also works with .kcpps config files, all settings are loaded into the existing GUI input fields. This can be used to load a common configuration while still allowing the user to edit one or two customized settings before starting the server.

### **What is `--preloadstory`**  
You can pass a Kobold Lite JSON file with this parameter when launching the KoboldCpp server. The save file will automatically be served and loaded to any new Kobold Lite clients who connect to your server, effectively giving you a preconfigured story that you can easily share over the network.

### **What is `--chatcompletionsadapter`**  
You can pass an optional ChatCompletions Adapter JSON file to force custom instruct tags when launching the KoboldCpp server. This is useful when using the OpenAI compatible Chat Completions API with third party clients. The adapter file takes the following JSON format, all fields are optional.

```
{
"max_length":512,
"system_start":"str",
"system_end":"str",
"user_start":"str",
"user_end":"str",
"assistant_start":"str",
"assistant_end":"str",
"tools_start":"str",
"tools_end":"str",
"add_sd_negative_prompt":"str",
"add_sd_prompt":"str",
}
```
KoboldCpp comes with a few built in adapters included for convenience. The `AutoGuess.json` adapter will try to heuristically infer the correct instruct template to be used for the chat completions endpoint, based on the detected Jinja template from the model.

### **How to use `--onready`**  
This is an advanced parameter intended for script or command line usage. You can pass a terminal command (e.g. start a python script) to be executed after Koboldcpp has finished loading. This runs as a subprocess, and can be useful for starting cloudflare tunnels, displaying URLs etc.

### **Phrase Banning (Anti-Slop): How do I stop my model from generating (specific symbol), e.g. `[` or specific phrases**  
Sometimes, you want to prevent a model from using a specific symbol, e.g. the left square bracket `[` like Kobold United does. Adding `[` to the Phrase/Token Ban field in Kobold Lite will prevent it from generating this specific substring. You can now provide a specified list of words or phrases prevented from being generated, by backtracking and regenerating when they appear. 
- Logit Bias: For advanced users. Setting `logit_bias` over the API allows you to prioritize or reduce the chance of specific token IDs appearing in the AI output, without banning it completely.

### **What is Smart Context?**  
Smart Context is enabled via the command `--smartcontext`. In short, this reserves a portion of total context space (about 50%) to use as a 'spare buffer', permitting you to do prompt processing much less frequently (context reuse), at the cost of a reduced max context.  
How it works: when enabled, Smart Context can trigger once you approach max context, *and* then send two consecutive prompts with enough similarity (e.g. the second prompt has more than half the tokens matching the first prompt). Imagine the max context size is 2048. When triggered, KoboldCpp will truncate away the first half of the existing context (top 1024 tokens), and 'shift up' the remaining half (bottom 1024 tokens) to become the start of the new context window. Then when new text is generated subsequently, it is trimmed to that position and appended to the bottom. The new prompt need not be recalculated as there will be free space (1024 tokens worth) to insert the new text while preserving existing tokens. This continues until all the free space is exhausted, and then the process repeats anew.

> Analogy: Imagine there is a Bus with a capacity for 50 seats. At each stop, 5 people want to get on. Now imagine that once the bus is full, the driver has to kick out the earliest 5 passengers off the bus, before the next 5 people can get on the bus. Assume kicking any number of people off the bus is very difficult and disruptive because they are slow and stubborn.
> So for the first 10 stops, everything is fine. But at stop 11, the bus is full, and then every stop after becomes slow due to kicking 5 off before 5 new can board.
> What if, instead of kicking 5 off when the bus is full, the driver kicks off half the bus (25 people)? That takes the same amount of time as kicking 5 people off. But then for the next 5 stops after that, people can board the bus in peace as there will be free space. This continues until the bus is full again, and then half the people get kicked out.
> That's smartcontext

### **What is ContextShift?**  
Context Shifting is a better version of Smart Context that only works for GGUF models. This feature utilizes KV cache shifting to automatically remove old tokens from context and add new ones without requiring any reprocessing. So long as memory is not changed or edited and you don't use world info, you should be able to avoid almost all reprocessing between consecutive generations even at max context. This does not consume any additional context space, making it superior to SmartContext. Context Shifting is enabled by default, and will override `smartcontext` if both are enabled. Your outputs may be different with shifting enabled, but both seem equally coherent. To disable Context Shifting, use the flag `--noshift`. 

### **What is FastForwarding?**  
Fast forwarding is enabled by default, and allows the AI to skip reused tokens in the context that have already been processed in the previous turn. To disable Fast Forwarding, use the flag `--nofastforward`. 
 
### **How do I make the AI handle longer context than 2048? Also, the Kobold Lite max context slider only goes up to 2048 / My koboldcpp crashed while processing a long prompt / How do I increase context size?**  
First, you need to allocate extra RAM for buffers when using extended context above 2048. Set `--contextsize` to the desired max context size you want to use, e.g. `--contextsize 4096` for a 4K context, or `--contextsize 8192` for 8K context limit. If you're using a GGUF model, your RoPE scaling should be automatically configured correctly. KoboldCpp supports a contextsize up to 16k for GGML models and 32k for GGUF models.  
You may also need to change the "Max Tokens" value in Kobold Lite beyond the default slider limit of 2048. To do so, click and edit the number above the Max Tokens slider, it is an editable text inputbox that can be overriden to a higher value beyond the slider range.

### **What is RoPE config? What is NTK-Aware scaling?  What values to use for RoPE config?**  
RoPE scaling (via `--ropeconfig`) is a novel technique capable of extending the useful context of existing models without finetuning. It can be used to stretch a model's context limit by over 4x (e.g. 2048 to 8192) with minor to moderate quality degradation.  
The default is `--ropeconfig 1.0 10000`, 1x unscaled. There are 2 scaling modes, which can be combined if desired.  
- Linear Scaling, set with the 'frequency scale`, the first parameter of `--ropeconfig`, e.g. for 2x linear scale, use `--ropeconfig 0.5 10000`, for 4x, use `--ropeconfig 0.25 10000`.
- NTK-Aware Scaling, set with 'frequency base`, the second parameter of `--ropeconfig`, e.g. `--ropeconfig 1.0 32000` for approx 2x scale, or `--ropeconfig 1.0 82000` for approx 4x scale. Experiment to find optimal values. If `--ropeconfig` is not set, NTK-Aware scaling is the default, automatically set based off your `--contextsize` value.

### **What is mmap**  
mmap, or memory-mapped file I/O, maps files or devices into memory. It is a method of reducing the amount of RAM needed for loading the model, as parts can be read from disk into RAM on demand. You can enable it with `--usemmap`

### **What is mlock**  
mlock is a technique used to force a model to remain in RAM after it has been loaded. On some systems, especially when RAM is scarce, the OS may trigger memory swapping too frequently, reducing performance. Setting `--usemlock` will prevent that from happening. mlock is disabled by default.

### **How do I use multiple GPUs?**  
Multi-GPU is only available when using CuBLAS. When not selecting a specific GPU ID after `--usecublas` (or selecting "All" in the GUI), weights will be distributed across all detected Nvidia GPUs automatically. You can change the ratio with the parameter `--tensor_split`, e.g. `--tensor_split 3 1` for a 75%/25% ratio.

### **What does lowvram do for CuBLAS**  
lowvram can be added to `--usecublas` to reduce VRAM usage at the cost of speed, by not offloading the scratch buffers and KV buffers. 
_Update Oct 2023: lowvram is no longer triggered in the newest GGUF models. It is still currently preserved for compatibility purposes with older GGML models._
_Update Jan 2024: lowvram is now in use again. If enabled, it prevents the per-layer KV offloading to GPU, KV will not be offloaded at all if enabled._

### **What does Quantized Mat Mul (MMQ) do for CuBLAS**  
`mmq` is an upstream feature can be added to `--usecublas` to use quantized matrix multiplication in CUDA during prompt processing, instead of using cuBLAS for matrix multiplication. Experimentally this uses slightly less memory, and is slightly faster for Q4_0 but slower for K-quants. However, for long prompts on new GPUs, cuBLAS is generally faster at the cost of slightly more VRAM (MMQ off). In newer versions, it is enabled by default, and you must use `nommq` to disable it instead if unwanted.

### **What's the difference between row and layer split**  
This only affects multi-GPU setups, and controls how the tensors are divided between your GPUs. The best way to gauge performance is to try both, but generally layer split should be best overall, while row split can help some older cards.

### **What is LoRA and LoRA Base**  
LoRA is an adapter model that can be applied on top of the weights of an existing model to modify them. This is generally not advised - you're instead recommended to merge the LoRA into the model before converting the end result into GGUF format for optimal quality. `--lora-base` is used so that you can apply the LoRA directly to a larger base model (like an f16 model) even if you can't fit it in memory. The LoRA changes weights of the model but it may change them in a way that is rounded differently on a quantized model versus the base model, so in general if you have the f16 model available you should apply the LoRA to that.  
Further reading: https://github.com/LostRuins/koboldcpp/discussions/514 and https://github.com/LostRuins/koboldcpp/pull/224

### **What is LLaVA and mmproj**  
`--mmproj` can be used to load a multimodal projector onto a model (e.g. LLaVA), allowing the model to have AI vision capabilities, to perceive and react to images you send it. You can get projectors for some popular architectures [at this link](https://huggingface.co/koboldcpp/mmproj/tree/main), though they are optimized for the LLaVA finetune.

### **Flash Attention**  
`--flashattention` can be used to enable flash attention when running with CUDA/CuBLAS, which can be faster and more memory efficient.

### **Quantized KV Cache**  
You can now utilize the Quantized KV Cache feature in KoboldCpp with `--quantkv [level]`, where `level 0=f16, 1=q8, 2=q4`. Note that quantized KV cache is only available if `--flashattention` is used, and is **NOT** compatible with Context Shifting, which will be disabled if `--quantkv` is used.

### **Speculative Decoding (Draft Models)**  
You can explore speculative decoding by loading a draft model. This is intended to be a smaller fast model with the same vocab as the big model, that tries to speed up inference by guessing tokens. Use `--draftmodel` to select the speculative decoding model.
  - `--draftgpulayers` - Set number of layers to offload for speculative decoding draft model
  - `--draftgpusplit` - GPU layer distribution ratio for draft model (default=same as main). Only works if using multi-GPUs.

### **Overriding MoE models**  
`--moeexperts` - Overwrite the number of experts to use in MoE models

### **What is Whisper?**  
Whisper is a speech-to-text model that can be used for transcription and voice control within Kobold Lite. Load a Whisper GGML model with `--whispermodel`. In Kobold Lite, uses microphone when enabled in settings panel. You can use Push-To-Talk (PTT) or automatic Voice Activity Detection (VAD) aka Hands Free Mode, everything runs locally within your browser including resampling and wav format conversion, and interfaces directly with the KoboldCpp transcription endpoint.

### **What is OuteTTS Text To Speech?**  
OuteTTS is a text-to-speech model that can be used for narration by generating audio within Kobold Lite. You need two models, an OuteTTS GGUF and a WavTokenizer GGUF which you can find [here](https://github.com/LostRuins/koboldcpp/wiki#getting-an-ai-model-file). Once downloaded, load them in the Audio tab or using `--ttsmodel` and `--ttswavtokenizer`. You can also use `--ttsgpu` to load them on the GPU instead, and `--ttsthreads` to set a custom thread count used.

### **Can I use SSL?**  
You can now import your own SSL cert to use with KoboldCpp and serve it over HTTPS with `--ssl [cert.pem] [key.pem]` or via the GUI. The `.pem` files must be unencrypted, you can also generate them with OpenSSL, eg. `openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365 -config openssl.cnf -nodes` for your own self signed certificate.

### **How can I see the data inside a GGUF file**  
KoboldCpp now allows you to use `--analyze` on any GGUF file, which will display the metadata and tensor names, dimensions and types within that file.

### **Can I add authentication?**  
You can add a password with the `--password` launch flag, which will require the user to request generations using an API key. You can also use a reverse proxy to provide it on the OpenAI API such as https://gitgud.io/khanon/oai-reverse-proxy

### **The program just closes and nothing is shown.**  
The program probably crashed, but the terminal closed too quickly to read the output. You should relaunch koboldcpp via the command prompt/terminal, and read the error message printed on the console. To do this, refer to the section "How to use the command line/terminal".

### **My AI continues rambling / writing rambling after it should have stopped generating / What does Unban Tokens do?**  
Some models will use a special "EOS" (End-Of-Stream) token to indicate when they have finished responding. That is often generated at the end of a paragraph, or when the AI doesn't know how to continue, or believes it has finished speaking. If this EOS token is banned, the model will continue generating indefinitely until the requested tokens are all consumed. You can toggle this behavior in the Kobold Lite Settings for `EOS Token Ban` (set to Auto or Unban to allow EOS), or by setting the `use_default_badwordsids` payload parameter to `false` when using the generate API.  Generally, EOS token unban is usually good for Instruct mode, situationally useful in Chat and Adventure mode, but should not be used in Story mode.  
_Note: `--unbantokens` has been deprecated and should not be used._

### **My model is generating nonsense/rubbish output!**  
This may be a bug, and if so, you should report it. However, there are a few options to check first:
- Make sure you are using a known good GGUF or GGML model. Bad quantizations do exist, especially some K-quants that have been incorrectly converted. Redownload a known good model from a reliable source.
- Make sure your RoPE config is applicable for the model you're using. Some models require specific `--ropeconfig` settings to function, such as 8K and 16K versions of SuperHOT. If the defaults don't work, try again with a different RoPE scale.
- Make sure your model is actually supported. Some architectures are not supported in KoboldCpp, or have been modified in non-standard ways for specific projects. Those GGML models will not work.
- Check your sampler order and sampler values. For more information, read the "Samplers" section of Kobold Lite below. Good defaults are Top-P=0.92, RepPen=1.1, Temperature=0.7 and a sampler order of [6,0,1,3,4,2,5].

### **My koboldcpp crashed whiled loading a model / WinError / I think I don't have AVX2 / Old CPU help / What is NoAvx2**  
Some older devices do not have support for AVX2, which is a required instruction for fast inference. KoboldCpp has a fallback option for such users, No AVX2 mode. To use this, launch via the command line (see how to above) with the flag `--noavx2`. Alternatively, in the GUI, select the "Old CPU, no AVX2" preset, and AVX1 instructions will be used instead. If it still doesn't work, as a last resort, you can try enabling "Failsafe" mode, with the flags `--failsafe` and see if that works. This is also selectable in the GUI (bottom option labelled Failsafe). Be aware that GPU support is not enabled for these modes and they will be significantly slower. Failsafe mode disables all CPU intrinsics and GPU usage.

### **I saw some error message about not enough space in the scratch memory / context memory / failed allocation**  
This is likely due to the context or scratch buffer size being insufficient for the current context. First, try reducing the max context size that you are using, and also try lowering `--blasbatchsize` to 128 or 64. If that still does not work, please file a bug report on Koboldcpp github.

### **Koboldcpp is not working on windows 7.**  
Windows 7 is not a recommended OS to use for KoboldCpp. If you still want to use it, you must use one of the fallback "Old CPU" modes, e.g. `--noavx2` or "Failsafe Mode" with `--failsafe` for it to work correctly, but it will be slow. You are recommended to upgrade your OS to Windows 10.

### **My GGML model is detected as the wrong type/version**  
This can happen if the model was incorrectly converted or quantized, or corrupted during download. Try downloading a fresh copy of the model. If it still fails, the version may be incorrectly detected - you can force it to a specific version with the `--forceversion` flag. Here is a reference of currently supported fileversions.
- GGML=1            original llama ggml, alpaca, GPT4ALL, GPTJ header
- GGHF=2            llama ggmf
- GGJT=3            llama ggjt
- GGJT_2=4          newer llama format unshuffled
- GGJT_3=5          using 16bit scalar
- GGUF_GENERIC=6    all gguf models v1 and v2
- GPTJ_1=100        the very first super old GPTJ format, pre-llama.cpp days
- GPTJ_2=101        pygmalion, uses old ggml lib
- GPTJ_3=102        uses new ggml lib
- GPTJ_4=103        unshuffled
- GPTJ_5=104        using 16bit scalar
- GPT2_1=200        ancient gpt2 format, pre-llama.cpp days
- GPT2_2=201    
- GPT2_3=202        unshuffled
- GPT2_4=203        using 16bit scalar
- RWKV_1=300    
- RWKV_2=301    
- NEOX_1=400    
- NEOX_2=401    
- NEOX_3=402        redpajama
- NEOX_4=403        unshuffled
- NEOX_5=404        unshuffled redpajama
- NEOX_6=405        using 16bit scalar
- NEOX_7=406        using 16bit scalar redpajama
- MPT_1=500         first supported mpt version
- GGUF_FALCON=600   falcon GGUF v1 and v2

### **Can I benchmark my system performance?**  
You can use `--benchmark`, which automatically runs a benchmark with your provided settings, outputting run parameters, timing and speed information as well as testing for coherence, and exiting on completion. You can provide a filename e.g. `--benchmark result.csv` and it will write CSV formatted data appended to that file.

### **What is `--prompt`**  
This flag can be to run KoboldCpp directly from the command line without running the server, the output of the prompt will be generated and printed into the terminal before exiting. When running with --prompt, all other console outputs are suppressed, except for that prompt's response which is piped directly to stdout. You can control the output length with --promptlimit. These 2 flags can also be combined with --benchmark, allowing benchmarking with a custom prompt and returning the response. Note that this mode is only intended for quick testing and simple usage, no sampler settings will be configurable.

### **Can I generate images with KoboldCpp?**  
Yes, KoboldCpp now natively supports Local Image Generation, thanks to stable-diffusion.cpp. It provides a ComfyUI and A1111 compatible txt2img endpoint which you can use within the embedded Kobold Lite, or in many other compatible frontends such as SillyTavern. 
  - Just select a compatible SD3, Flux, SD1.5 or SDXL `.safetensors` model to load, either through the GUI launcher or with `--sdmodel`
  - Note: VAEs and LoRAs should be baked inside the model itself, unless you specify them with `--sdvae`,`--sdvaeauto` or `--sdlora`. FP16 is recommended.
  - Supported flags:
```
--sdmodel     Specify a stable diffusion model to enable image generation.
--sdthreads   Use a different number of threads for image generation if specified. 
--sdquant     If specified, loads the model quantized to save memory.
--sdclamped   If specified, limit generation steps and resolution settings for shared use. Optionally allows setting max size.
--sdlora      If specified, tries to load a Stable Diffusion LoRA model
--sdloramult  Set the LoRA multiplier
--sdvae       Set a custom VAE
--sdvaeauto   Use built in fallback VAE (TAESD)
--sdnotile    Disable VAE tiling
--sdt5xxl     For Flux and SD3, you need to load a T5-XXL language model as well. Some files bundle it with the main model.
--sdclipl     For Flux and SD3, you need to load a Clip-L model as well. Some files bundle it with the main model.
--sdclipg     For SD3, you need to load a Clip-L model as well. Some files bundle it with the main model.
```
  - For a quick example, [here are some known working Image Generation models you can try](https://github.com/LostRuins/koboldcpp/wiki#getting-an-ai-model-file)
  - If you're running a shared server, it's recommended to use both `--sdclamped` and `--sdquant` to avoid running out of memory.

## Kobold Lite Web UI

<img src="https://github.com/LostRuins/koboldcpp/assets/39025047/7845b69e-b5a5-4de5-8fb5-0d39b68b441d" width="600">  

*(Image guide originally from /lmg/, thanks anon)*

### **What is Kobold Lite? How do I use it?**  
Kobold Lite is a lightweight, standalone Web UI for KoboldCpp, KoboldAI Client, and AI Horde, which requires no dependencies, installation or setup. It comes pre-bundled with all distributions of KoboldCpp and is ready to use out of the box. After starting KoboldCpp (default port is 5001), just navigate your local browser such as Chrome, Firefox or Safari to http://localhost:5001 and Kobold Lite will be launched.

### **Basic Modes of Kobold Lite**  
Kobold Lite has 4 different modes, which you can toggle using the 'Format' Dropdown inside the "Basic Settings" panel. 
- Story Mode: For creative fiction and novel writing, the AI continues your story based on your input.
- Chat Mode: Simulates a character persona with an interactive AI chatbot. Ask the AI anything, or chit-chat with it in turn based conversation.
- Instruct Mode: ChatGPT styled instruction-response. Give the AI a task, and it will try to fulfill the instruction.
- Adventure Mode: AIDungeon styled interactive fiction, choose-your-own-adventure, describe an action and the AI narrates the result.
The best way to get started after launching Kobold Lite is to jump into a pre-crafted **Scenario**, which you can select from the "Scenarios" button.

### **UI Style Select**  
In newer Kobold Lite versions, you can pick from 3 different UIs (not all are available in all modes).
- Classic: This is the default Kobold notepad look and feel, simple, clean, efficient, and available for all modes.
- Messenger: This is an alternative UI for chat mode, which shows up as a messenger style chat between you and the AI.
- Aesthetic: This is an alternative UI for chat and instruct mode, which allows great customization of text styles, colors, padding and inclusion of image portraits.
- Corpo: This UI attempts to mimic the look and feel of Corporate AI Assistants such as ChatGPT.

### **What are samplers? How do I change or disable them? What are the best samplers?**  
Samplers are basically how the AI determines the next token to choose, from the list all possible tokens. There are many different samplers with different properties, though you will generally only need a few. Good defaults to use are Top-P=0.92, RepPen=1.1, Temperature=0.7 and a sampler order of [6,0,1,3,4,2,5], leaving everything else disabled (default).  
- Top-K: This setting limits the number of possible words to choose from to the top K most likely options, removing everything else. Can be used with Top-P. Set value to 0 to disable its effect.
- Top-A: Alternative to Top-P. Remove all tokens that have softmax probability less than top_a*m^2 where m is the maximum softmax probability. Set value to 0 to disable its effect.
- Top-P: Discards unlikely text in the sampling process. Only considers words with the highest cumulative probabilities summing up to P. Low values make the text predictable, as uncommon tokens are removed. Set value to 1 to disable its effect.
- TFS: Alternative to Top-P, this setting removes the least probable words from consideration during text generation, considering second order derivatives. Can improve the quality and coherence of the generated text.
- Typical: Selects words randomly from the list of possible words, with each word having an equal chance of being selected. This method can produce text that is more diverse but may also be less coherent. Set value to 1 to disable its effect.
- Temperature: Controls how 'Random' the output is by scaling probabilities without removing options. Lower value are more logical, but less creative.
- Repetition Penalty: Applies a penalty to reduce usage of words that have already been used recently, making the output of the AI less repetitive.
- Mirostat: Alternative sampling method that overrides other samplers. See mirostat section.
- Min-P: An experimental alternative to Top-P that removes tokens under a certain probability. Set value to 0 to disable its effect.
- DynaTemp: Dynamic Temperature Sampling is a variant of normal Temperature sampling where the temperature is allowed to automatically vary between two preset limits. Temperature is allowed to be automatically adjusted dynamically between DynaTemp ± DynaTempRange. Set DynaTemp Range to 0, or set min and max to the same value, to disable it.
- DRY: DRY is a dynamic N-gram anti-repetition sampler, used as an alternative or together with Repetition Penalty. Only recommended for advanced users.
- XTC:  XTC (Exclude Top Choices) sampler is creative writing sampler designed by the same author of DRY. It removes common tokens with high probability when there are many choices, allowing for more creative and flavorful text. To use it, increase xtc_probability above 0 (recommended values to try: xtc_threshold=0.15, xtc_probability=0.5)

### **What is sampler order? What is the best sampler order? I got a warning for bad suboptimal sampler orders.**  
Sampler order controls the order in which the above samplers are applied in sequence, to the list of token candidates when choosing the next token. It is **STRONGLY** not advised to change this from the default of [6,0,1,3,4,2,5] as that can lead to very poor outputs.

### **What are Logprobs? Can I view token probabilities?**  
You can now use the built-in Token Probability Viewer to display token probabilities, based on returned logprobs. This allows you to visualize alternative possible tokens that the AI could have chosen for every token in the returned output.

### **What are custom presets?**  
Presets are pre-configured sampler settings that have been contributed or collected over time to emulate specific writing styles or platforms. Some of them have sub-optimal configurations or sampler orders, but they should be considered artistic rather than practical - you will likely still get optimal results from the default preset.

### **Max Ctx. Tokens (Context Size)**  
Context size determines the maximum number of tokens (context window) that will be sent to the AI, in other words, it controls how far back in, and how much of the text the AI gets to access, remember and use. Most models are limited to 2048 tokens of context, but some have been trained with larger context sizes. Bigger contexts take more memory and are slower to process and generate with. To extend context, refer to the sections on "longer context above 2048" and "RoPE scaling". This field can be manually overridden past the slider limit by editing the text input field.

### **Amount to Generate**  
Maximum number of tokens the AI can generate for it's response to each submitted request. Each token is roughly about four letters long.

### **Token Streaming**  
Enable this option to allow tokens from an incomplete AI response to be gradually streamed into the UI instead of only responding when the generation is complete. Not applicable for AI Horde users.

### **Trim Whitespace**  
This option combines multiple consecutive newlines into one single newline. It also removes trailing whitespace at the end of the submitted prompt.

### **Trim Sentences**  
This option trims the AI's response down to the last complete sentence, if possible.

### **EOS Token Ban**  
This option controls the AI's usage of the End-Of-Stream Token, a special token that lets the AI stop responding early when it thinks the response is complete. It replaces the old `--unbantokens` launcher flag.  
- Auto: Automatically determine whether to use EOS tokens or not.
- Unban: Always allow the EOS token to be used.
- Ban: Prevent the EOS token from being generated.

### **Placeholder Tags**  
This option allows the placeholder tags `{{user}}` `{{char}}` `{{[INPUT]}}` and `{{[OUTPUT]}}` to be used by character card or scenario authors, which will be dynamically replaced with the correct value on runtime. For example, `{{char}}` will get replaced with the chatbot's selected nickname.

### **Persist Autosave Session**  
This option autosaves your story and settings, which will be restored the next time you start KoboldCpp again. However, to avoid data loss you are still recommended to manually export your saved story .json files from time to time.

### **Save File Includes Settings**  
This option allows your Kobold Lite UI, generation and sampler settings to be saved directly into the story json file itself, and loaded again in future.

### **Show Rename Save File**  
This option triggers a popup when you save your story, allowing you to rename the target save file name.

### **Autoscroll Text**  
This option scrolls down the text window to the bottom every time a new AI response is received.

### **Invert Colors**  
This option inverts all the colors for the UI, useful for e-ink displays or people who prefer a light theme.

### **Chat/Story - Idle Responses**  
Enabling this option allows the AI to automatically send new responses after the player has been idle for a few seconds, useful to simulate a real-time chat conversation.

### **Chat - Multiline Replies**  
This allows the AI to respond to your chat messages with more than a single-line response. This may result in more verbose and lengthy chat responses, but the output can also become wildly incoherent and unpredictable, or the AI might even start talking as someone else. **Not recommended for beginners**.

### **Chat - Continue Bot Replies**  
This option allows the AI to stop speaking halfway (incomplete reply), and then resume speaking within the same message, when you press the submit button again. If disabled, each response from the AI will instead start on a new line with the AI name prefix added (IRC style). Enabling 'Continue Bot Replies' may result in the AI refusing to speak if it does not know what to say. **Not recommended for beginners**.

### **Chat - Your Name / AI Name**  
You can set your displayed name and the AI name for the current chat session, useful for roleplaying specific characters.

### **Instruct - Start and End Sequence**  
Set this to the Instruct start and end instruct sequences that the model was trained on for best quality. For Alpaca, this is `### Instruction: ` and `### Response: `, which should generally work well for most instruct models. You can add newlines with `\n` if desired.

### **Instruct - Enable Markdown**  
This allows instruct mode to generate formatted markdown, such as item lists, tables and code blocks. Useful for coding tasks.

### **Adventure - Adventure Prompt**  
This option injects a pre-prompt to the AI to make it take adventure mode more seriously, useful especially if your prompt is short. **Highly recommended to keep enabled for beginners, unless using a custom scenario.**

### **How do I make the AI remember things?**  
As contexts gets very long, eventually the earlier parts of your story will exceed the maximum context length and get trimmed away. There are some features in the 'Memory' panel to preserve the overall aspets of your story in such scenarios.  
- Memory - This is a sequence of text that will always be injected into the start of each prompt sent to the AI. It is useful for things the AI should always remember even over very long stories, such as main theme(s) of your story, the broad strokes of the setting, central conflict(s), and protagonist. As it uses up context space, try to keep Memory short, at most a paragraph or two.
- Author's Note - This is similar to memory, but is injected *near* the *end* of the prompt rather than at the start. It's used to describe recent situations, or guide the AI to behave in a certin way for the current scene. A/N Strength affects how far back this text is injected.
- World Info - This is text that is only situationally injected into the prompt. When the World Info "Key" is matched, the corresponding "Content" text gets injected into the start of the prompt. Useful for reminding the AI of facts, character names, ages, personalities, places as well as plot points, like a dictionary or encyclopedia.

### **What are stop sequences (stopping tokens)?**  
Stop Sequences are a set of specially designated tokens or phrases that should make the model stop generating early. For example, if you wanted the output to end after a new paragraph, you could use `\n\n` as a stopping sequence. Chat mode, Instruct mode and Adventure mode all come with preconfigured stop sequences.

### **What are the buttons above the user text input box?**  
- Back - This functions like an Undo button, reversing the most recent action or AI response.
- Redo - This is a Redo button, which reverses the 'Back' button and restores deleted text from history.
- Retry - This button retries your most recent action or message, useful if you don't like the AI response and want something different.
- Edit - This is not a button but a checkbox toggle. When enabled, you'll be able to retroactively modify any part of your existing story, or the response from the AI.

### **My chat mode is malfunctioning. How do I stop the AI from replying as myself?**  
This can happen when the model is poorly prompted, especially with 'Multiline Replies' enabled. Often, the solution is just to retry the most recent request. However, here are some tips to avoid this:  
- Disable 'Multiline Replies'
- Use a good model, preferably finetuned on chat conversations
- Make sure the initial prompt or character card is well formatted. Names should be consistent, well-formatted layout wise, and not misspelled. A few good examples in memory goes a long way, if the chat history is bad, the chat future will be bad too.
- In extreme cases, set your chat username as a custom stopping token. This will have unintended side effects.

### **My AI response is very short / the AI response in the console is longer, some words got trimmed from the terminal to the UI.**  
This is the opposite problem to the above, sometimes the AI has many interesting things to say, but they get trimmed away because it responded across multiple lines or even multiple paragraphs. Enabling 'Multiline Replies' allow such responses to be used. Remember - the AI learns from examples. A boring prompt or dull messages from the user can lead to dull AI replies.

### **What is AI Vision?**  
AI Vision is an attempt to provide multimodality by allow the model to recognize and interpret uploaded or generated images. This uses AI Horde or a local A1111 endpoint to perform image interrogation, similar to LLaVa, although not as precise. Click on any image and you can enable it within Lite. This functionality is not provided by KCPP itself.

### **What file formats does Kobold Lite support?**  
Kobold Lite supports many file formats, automatically determined when the file is loaded. These include:
- KoboldAI Classic .json saves (Default)
- KoboldAI United .json saves (V2 format)
- KoboldAI KAISTORY files
- TavernAI and SillyTavern Character Cards (JSON format, WebP and PNG all supported)
- Oobabooga charaacter and story exports
- Agnai and Tavern world info formats
- Raw text files

### **Where can I find the source code for Kobold Lite? What about the online version?**  
The source code for Kobold Lite is under AGPLv3, and [can be found here](https://github.com/LostRuins/lite.koboldai.net).
The web version powered by Horde can be accessed at https://lite.koboldai.net

### **Can I run a UI without Javascript, (e.g. from a very old browser) or over the command line (e.g. SSH?)**  
You can use KoboldCpp NoScript WebUI, which does not require Javascript to work. It should be W3C HTML compliant and should run on every browser in the last 20 years, even text-based ones like Lynx (e.g. in the terminal over SSH). It is accessible by default at `/noscript` e.g. `http://localhost:5001/noscript` . This can be helpful when running KoboldCpp from systems which do not support a modern browser with Javascript.

## KoboldCpp Integrations  
### **What is KoboldAI United? How to use KoboldAI Client / Kobold United?**  
[KoboldAI United](https://github.com/henk717/KoboldAI) is the current actively developed version of KoboldAI, while [KoboldAI Client](https://github.com/KoboldAI/KoboldAI-Client) is the classic/legacy (Stable) version of KoboldAI that is no longer actively developed.  
KoboldCpp maintains compatibility with both UIs, that can be accessed via the `AI/Load Model > Online Services > KoboldAI API` menu, and providing the URL generated after launching KoboldCpp.  

### **What is Horde? How do I use it? How do I share my model with Horde?**  
The AI Horde is a crowdsourced distributed cluster of Image generation workers and Text generation workers, where people can share their own processing power to generate images and text for other users. KoboldCpp now comes included with an embedded *lightweight Horde Worker* which allows anyone to share their ggml models with the AI Horde without downloading additional dependences apart from KoboldCpp.
- To use Horde as an end-user, you can go to https://lite.koboldai.net
- To share your own models and compute power over Horde using Koboldcpp:
  - Register for an [AI Horde API key](https://horde.koboldai.net/register).
  - Enable the Horde config from the GUI and fill in all details, or launch by setting `--hordekey`, `--hordemodelname` and `--hordeworkername` which will start a Horde worker for you that serves horde requests automatically in the background. 
  - Exclude your `--hordekey` to continue using your own standalone Horde worker (e.g. Haidra Scribe / KAI Horde Bridge).
  - Supported Flags:
```
--hordemodelname  Sets your AI Horde display model name.
--hordeworkername Sets your AI Horde worker name.
--hordekey        Sets your AI Horde API key.
--hordemaxctx     Sets the maximum context length your worker will accept.
--hordegenlen     Sets the maximum number of tokens your worker will generate.
```

### **I'm encountering SSL errors with my horde worker**  
You can try `--nocertify` mode which allows you to disable SSL certificate checking on your embedded Horde worker. This can help bypass some SSL certificate errors.

### **What is SillyTavern? What is Pygmalion? What is Agnaistic? How do I use them?**  
SillyTavern and Agnaistic are third-party frontend user interfaces that specialize in interaction with chat/roleplay with AI characters. They include support for KoboldCpp as a backend, via the KoboldAI API. Pygmalion is a community that focuses on using AI for chat, they also have created their own finetuned chat model. In the 'Other established resources' references below you can find documentation for using Pygmalion and SillyTavern together with KoboldCpp.

### **How can I use the Kobold API? Is there an API reference? How does the KoboldCpp API differ from the KoboldAI United API?**  
The KoboldAI web API is the interface which downstream applications can communicate with KoboldCpp. The full KoboldCpp API reference can be found at https://lite.koboldai.net/koboldcpp_api as well as within the program by visiting `http://localhost:5001/api`. 
- In general, the most important endpoint is `/api/v1/generate`, which is the endpoint used to send prompts and receive responses from the AI. 
- Other useful endpoints are `/api/v1/model`, `/api/v1/config/max_length` and `/api/v1/config/max_context_length`
- In addition, KoboldCpp also implements a few additional endpoints not found in the original KoboldAI API, these include 
  - `/api/extra/generate/stream` for SSE streaming
  - `/api/extra/version` for version information 
  - `/api/extra/perf` for performance and timing information
  - `/api/extra/abort` to abort an in-progress generation
  - `/api/extra/generate/check` to get the partially completed text for an in-progress generation
  - `/api/extra/tokencount` to tokenize and accurately measure how many tokens any string has.
  - `/api/extra/true_max_context_length` to get the actual ctx length loaded from the launcher.

### **Is there an OpenAI API?**  
Yes, as of v1.45.2, there is now a simple OpenAI compatible completions API, which will allow KoboldCpp to be used with other projects that require an OpenAI API, you can access it at `/v1/completions` and `/v1/chat/completions` or view the [online API reference](https://lite.koboldai.net/koboldcpp_api). You're still recommended to use the Kobold API as it has many more settings.

### **Is there an Ollama API?**  
Yes, there is now a simple Ollama compatible API, which will allow KoboldCpp to be used with other projects that require Ollama specifically. For normal usage, this is NOT recommended, and only exists to provide unparalleled larger ecosystem compatibility.

### **What is WebSearch**  
When WebSearch is enabled, KoboldCpp now optionally functions as a WebSearch proxy with a new `/api/extra/websearch` endpoint, allowing your queries to be augmented with web searches. Works with all models, needs top be enabled both on Lite and on Kcpp with `--websearch` or in the GUI. The websearch is executed locally from the KoboldCpp instance, and is powered by DuckDuckGo.

### **Can I Talk To or Search my Documents**  
KoboldCpp offers a TextDB Document Lookup in KoboldAI Lite - This is a very rudimentary form of browser-based RAG. You can access it from the Context > TextDB tab. It's powered by a text-based minisearch engine, you can paste a very large text document which is chunked and stored into the database, and at runtime it will find relevant snippets to add to the context depending on the query/instruction you send to the AI. You can use the historical context as a document, or paste a custom text document to use. Note that this is NOT an embedding model, it uses lunr and minisearch for retrieval scoring instead. 

### **Are my chats private? What is with the Share button?**  
KoboldCpp is capable of running fully locally offline without internet, and does not send your inputs to anywhere else. Generated content using the API is displayed in the terminal console, which is cleared when the application is closed. Likewise, Kobold Lite UI will store your content only locally within the browser, it is not sent to any other external server. KoboldCpp and Kobold Lite are fully open source with AGPLv3, and you can compile from source or review it on github.  

If you use KoboldCpp with third party integrations or clients, they may have their own privacy considerations. When using Horde, your responses are sent between the volunteer and the user over the horde network and potentially can be read from either end, so do not send privacy sensitive information with Horde.

The "Share" button in Kobold Lite does not actually upload any data anywhere, rather it compresses your entire story into a very long URL (which encoded the data within it), that can be reloaded on a different device using the web version of Kobold Lite.

---

### Useful Links and References  
[Latest KoboldCpp Release for Windows](https://github.com/LostRuins/koboldcpp/releases/latest)  
[KoboldCpp repo and Readme](https://github.com/LostRuins/koboldcpp)  
[Github Discussion Forum](https://github.com/LostRuins/koboldcpp/discussions) and [Github Issues list](https://github.com/LostRuins/koboldcpp/issues?q=)  

### Other established resources  
[Local LLM guide from /lmg/, with good beginner models](https://rentry.org/local_LLM_guide)  
[SillyTavern documentation regarding KoboldAI](https://docs.sillytavern.app/usage/api-connections/koboldcpp/)  
[PygmalionAI documentation regarding KoboldAI](https://docs.pygmalion.chat/en/backend/kobold-cpp)  
[KoboldAI Discord Server](https://koboldai.org/discord)  
Also check out /lmg/, r/KoboldAI and r/LocalLLaMA/  

### Misc. Guides  
[Installing KoboldCpp on Android via Termux](https://www.reddit.com/r/KoboldAI/comments/14uxmsn/guide_how_install_koboldcpp_in_android_via_termux/)  
[Installing KoboldCpp on Linux with GPU](https://www.reddit.com/r/LocalLLaMA/comments/13q6u9e/koboldcpp_linux_with_gpu_guide/)  
[Building KoboldCpp CUDA on Linux](https://www.reddit.com/r/LocalLLaMA/comments/14faz1d/building_koboldcpp_cuda_on_linux/)  
[Simple Windows Guide to getting started with KoboldCpp](https://www.reddit.com/r/singularity/comments/144th3k/incredibly_simple_guide_to_run_language_models/)  
[Simplified LLAMA Guide](https://rentry.org/TESFT-LLaMa#koboldcpp-windows)  
[Compiling on Windows, A quick guide](https://github.com/LostRuins/koboldcpp/issues/664)
[Guide to Using the API](https://www.reddit.com/r/LocalLLaMA/comments/1hx8gid/a_beginners_guide_to_llm_scripting_using_python/)

### Notable Forks (They may have special features)  
https://github.com/henk717/koboldcpp  
https://github.com/ycros/koboldcpp  
https://github.com/YellowRoseCx/koboldcpp-rocm  
https://github.com/0cc4m/koboldcpp  
https://github.com/SammCheese/koboldcpp  