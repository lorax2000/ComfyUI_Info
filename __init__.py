import os
import platform
import subprocess

TAG = "ComfyUI_Cmds"

class CmdExecutor:
    @classmethod
    def INPUT_TYPES(s):
        system_info = f"System: {platform.system()} {platform.release()}"
        print(f"{TAG}: {system_info}")
        return {
            "required": {
                "command": ("STRING", {"default": "", "multiline": True}),
                "system_info": ("STRING", {"default": system_info}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute_command"
    CATEGORY = "system"
    OUTPUT_NODE = True

    def execute_command(self, command ,system_info):
        try:
            # Execute command
            if platform.system() == "Windows":
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            else:
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            stdout, stderr = process.communicate()
            
            # Prepare output
            result = stdout
            if stderr:
                result += f"\n\nErrors:\n{stderr}"
                
            print(f"{TAG}: cmmresult {result}")
            return (result,)
            
        except Exception as e:
            print(f"{TAG}: cmmresult {e}")
            return (f"Error executing command: {str(e)}",)

NODE_CLASS_MAPPINGS = {
    "CmdExecutor": CmdExecutor
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CmdExecutor": "Command Executor"
}
