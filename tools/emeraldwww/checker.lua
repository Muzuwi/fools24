console:log("Lua based local checker for challenge 4 by TheZZAZZGlitch")

actions = {}

function readSolution()
    for line in io.lines("/mnt/prog/Programming/Challenges/fools24/tools/emeraldwww/solution_attempt2.txt") do
        if string.sub(line, 1, 1) == ";" then
            -- year 2024, still no continue statement
            goto continue
        end
        local fields = {}
        for field in (line .. " "):gmatch("%w+") do
            table.insert(fields, field)
        end
        if #fields < 2 then
            goto continue
        end
        local frame = tonumber(table.remove(fields, 1), 10)
        local addr = tonumber(table.remove(fields, 1), 16)
        if actions[frame] == nil then
            actions[frame] = {}
        end
        while #fields > 0 do
            val = tonumber(table.remove(fields, 1), 16)
            if addr > 0x3FFFFFF then
                console:log(string.format(
                    "[!] Write to $%.8X not allowed.",
                    addr
                ))
            elseif addr < 0x2000000 then
                console:log(string.format(
                    "[!] Write to $%.8X not allowed.",
                    addr
                ))
            elseif val > 0xff or val < 0 then
                console:log(string.format(
                    "[!] Not a valid value: $%.2X",
                    val
                ))
            else
                local s = {}
                s["addr"] = addr
                s["val"] = val
                table.insert(actions[frame], s)
            end
            addr = addr + 1
        end
        ::continue::
    end
end

function noInput()
    emu:clearKeys(0xffffffff)
end

function printTaskList()
    TASK_COUNT = 16
    TASK_SIZE = 4 + 1 + 1 + 1 + 1 + 16*2

    console:log("===== TASK LIST =====")
    for i=0x03005e00,0x03005e00 + TASK_COUNT*TASK_SIZE,TASK_SIZE do
        idx = (i - 0x03005e00) / TASK_SIZE
        ptr = emu:read32(i)
        is_active = emu:read8(i + 4)
        previous = emu:read8(i + 5)
        next = emu:read8(i + 6)
        console:log(string.format(
            "[offset %08x] Task %02d: %08x, isActive: %d, previous: %02x, next: %02x",
            i, idx, ptr, is_active, previous, next))
    end
end

function printMain()
    addr = 0x030022c0

    console:log("===== gMain =====")
    console:log(string.format("callback1: %08x",
                              emu:read32(addr + 0x0)))
    console:log(string.format("callback2: %08x",
                              emu:read32(addr + 0x4)))
    console:log(string.format("savedCallback: %08x",
                              emu:read32(addr + 0x8)))
end

function printSaves() 
    console:log("===== saveptr1 =====")
    console:log(string.format("national: %02x",
                              emu:read8(0x03005daa)))
    console:log(string.format("pokedex[owned]: %08x",
                              emu:read32(0x03005db8)))
    console:log(string.format("pokedex[seen]: %08x",
                              emu:read32(0x03005dec)))
end


function muzuwisFancyDebuggingSetup()
    -- printTaskList()
    -- printMain()
    printSaves()
end

function runFrame()
    local frameIndex = emu:currentFrame()
    buf:setName("FRAME: " .. frameIndex)
    if actions[frameIndex] ~= nil then
        for _, action in pairs(actions[frameIndex]) do
            console:log(string.format(
                "[frame %i] Setting $%.8X to $%.2X",
                frameIndex, action.addr, action.val
            ))
            emu:write8(action.addr, action.val)

            muzuwisFancyDebuggingSetup()
        end
    end

    muzuwisFancyDebuggingSetup()
end

buf = console:createBuffer("IMPORTANT")
buf:print("IMPORTANT INFORMATION:\n")
buf:print("If you wish to reload the script (for example, because you changed\n")
buf:print("your solution), remember to reset the Lua interpreter first by\n")
buf:print("choosing File -> Reset.\n")
buf:print("Only then reload the script with File -> Load.\n")
buf:print("Otherwise, your memory writes might get duplicated.")

console:log("Reading solution.txt...")
readSolution()
console:log("Running your solution (feel free to speed up emulation)")
cbFrame = callbacks:add("frame", runFrame)
cbKeys = callbacks:add("keysRead", noInput)
emu:reset()
