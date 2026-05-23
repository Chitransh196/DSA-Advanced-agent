# import subprocess
# import tempfile
# import sys


# def extract_code(user_input):
#     if "```" not in user_input:
#         return None

#     parts = user_input.split("```")
#     if len(parts) < 2:
#         return None

#     code = parts[1].strip()

#     if code.startswith("python"):
#         code = code[6:].strip()

#     return code


# def run_code(user_input):
#     code = extract_code(user_input)

#     if not code:
#         return "⚠️ Provide code inside triple backticks."

#     try:
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as f:
#             f.write(code)
#             file_path = f.name

#         result = subprocess.run(
#             [sys.executable, file_path],
#             capture_output=True,
#             text=True,
#             timeout=5
#         )

#         if result.stderr:
#             return f"❌ Error:\n{result.stderr}"

#         output = result.stdout.strip()
#         if output:
#             return f"✅ Output:\n{output}"

#         return "✅ Code executed successfully."

#     except Exception as e:
#         return f"❌ Execution failed: {e}"

import subprocess
import tempfile
import sys
import os


# --------- Extract Code ---------
def extract_code(user_input):
    if "```" not in user_input:
        return None

    parts = user_input.split("```")
    if len(parts) < 2:
        return None

    code = parts[1].strip()

    # Remove language (python, Python, etc.)
    lines = code.split("\n")
    if lines[0].lower().startswith("python"):
        code = "\n".join(lines[1:])

    return code.strip()


# --------- Safety Check ---------
def is_safe_code(code: str) -> bool:
    dangerous_keywords = [
        "import os", "import sys", "subprocess", "shutil",
        "open(", "eval(", "exec(", "__import__",
        "os.", "sys.", "globals()", "locals()"
    ]

    code_lower = code.lower()
    return not any(keyword in code_lower for keyword in dangerous_keywords)


# --------- Run Code ---------
def run_code(user_input):
    code = extract_code(user_input)

    # fallback: allow plain code (optional)
    if not code:
        code = user_input.strip()

    if not code:
        return "⚠️ No code provided."

    # 🚨 SAFETY CHECK
    if not is_safe_code(code):
        return "❌ Unsafe code detected! Execution blocked."

    try:
        # Create temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as f:
            f.write(code)
            file_path = f.name

        # Execute code
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True,
            timeout=5
        )

        # Cleanup temp file
        os.remove(file_path)

        # Handle errors
        if result.stderr:
            return f"❌ Error:\n{result.stderr.strip()}"

        output = result.stdout.strip()

        if output:
            return f"✅ Output:\n{output}"

        return "✅ Code executed successfully."

    except subprocess.TimeoutExpired:
        return "❌ Code execution timed out (possible infinite loop)."

    except Exception as e:
        return f"❌ Execution failed: {e}"
    
    