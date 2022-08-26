import vulkan as vk
import sdl2
import sdl2.ext
import ctypes

WIDTH = 400
HEIGHT = 400

window = sdl2.SDL_CreateWindow(
    'Game of Life'.encode('ascii'),
    sdl2.SDL_WINDOWPOS_UNDEFINED,
    sdl2.SDL_WINDOWPOS_UNDEFINED, WIDTH, HEIGHT, 0)

wm_info = sdl2.SDL_SysWMinfo()
sdl2.SDL_VERSION(wm_info.version)
sdl2.SDL_GetWindowWMInfo(window, ctypes.byref(wm_info))

# Instance Creation

appInfo = vk.VkApplicationInfo(
    sType=vk.VK_STRUCTURE_TYPE_APPLICATION_INFO,
    pApplicationName="Game of Life",
    applicationVersion=vk.VK_MAKE_VERSION(0, 1, 0),
    pEngineName="No Engine",
    engineVersion=vk.VK_MAKE_VERSION(0, 1, 0),
    apiVersion=vk.VK_API_VERSION_1_0)

extensions = vk.vkEnumerateInstanceExtensionProperties(None)
extensions = [e.extensionName for e in extensions]
print("availables extensions: %s\n" % extensions)