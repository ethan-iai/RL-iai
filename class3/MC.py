# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

# Tutorial sample #7: The Maze Decorator

try:
    from malmo import MalmoPython
except:
    import MalmoPython

import os
import sys
import time
import json
import numpy as np
import random
from priority_dict import priorityDictionary as PQ


# sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

def GetMissionXML(seed, gp, size=10):
    return '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

              <About>
                <Summary>Hello world!</Summary>
              </About>

            <ServerSection>
              <ServerInitialConditions>
                <Time>
                    <StartTime>1000</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime>
                </Time>
                <Weather>clear</Weather>
              </ServerInitialConditions>
              <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"/>
                  <DrawingDecorator>
                    <DrawSphere x="-27" y="70" z="0" radius="30" type="air"/>
                  </DrawingDecorator>
                  <MazeDecorator>
                    <Seed>''' + str(seed) + '''</Seed>
                    <SizeAndPosition width="''' + str(size) + '''" length="''' + str(size) + '''" height="10" xOrigin="-32" yOrigin="69" zOrigin="-5"/>
                    <StartBlock type="emerald_block" fixedToEdge="true"/>
                    <EndBlock type="redstone_block" fixedToEdge="true"/>
                    <PathBlock type="diamond_block"/>
                    <FloorBlock type="air"/>
                    <GapBlock type="air"/>
                    <GapProbability>''' + str(gp) + '''</GapProbability>
                    <AllowDiagonalMovement>false</AllowDiagonalMovement>
                  </MazeDecorator>
                  <ServerQuitFromTimeUp timeLimitMs="30000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>

              <AgentSection mode="Survival">
                <Name>CS175AwesomeMazeBot</Name>
                <AgentStart>
                    <Placement x="0.5" y="56.0" z="0.5" yaw="0"/>
                </AgentStart>
                <AgentHandlers>
                    <DiscreteMovementCommands/>
                    <AgentQuitFromTouchingBlockType>
                        <Block type="redstone_block"/>
                    </AgentQuitFromTouchingBlockType>
                    <ObservationFromGrid>
                      <Grid name="floorAll">
                        <min x="-10" y="-1" z="-10"/>
                        <max x="10" y="-1" z="10"/>
                      </Grid>
                  </ObservationFromGrid>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''


def load_grid(world_state):
    """
    Used the agent observation API to get a 21 X 21 grid box around the agent (the agent is in the middle).

    Args
        world_state:    <object>    current agent world state

    Returns
        grid:   <list>  the world grid blocks represented as a list of blocks (see Tutorial.pdf)
    """
    while world_state.is_mission_running:
        # sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        if len(world_state.errors) > 0:
            raise AssertionError('Could not load grid.')

        if world_state.number_of_observations_since_last_state > 0:
            msg = world_state.observations[-1].text
            observations = json.loads(msg)
            grid = observations.get(u'floorAll', 0)
            break
    return grid


def find_start_end(grid):
    """
    Finds the source and destination block indexes from the list.

    Args
        grid:   <list>  the world grid blocks represented as a list of blocks (see Tutorial.pdf)

    Returns
        start: <int>   source block index in the list
        end:   <int>   destination block index in the list
    """
    start = grid.index(u'emerald_block')
    end = grid.index(u'redstone_block')
    return (start, end)
    # -------------------------------------
def extract_action_list_from_path(path_list):
    """
    Converts a block idx path to action list.

    Args
        path_list:  <list>  list of block idx from source block to dest block.

    Returns
        action_list: <list> list of string discrete action commands (e.g. ['movesouth 1', 'movewest 1', ...]
    """
    action_trans = {-21: 'movenorth 1', 21: 'movesouth 1', -1: 'movewest 1', 1: 'moveeast 1'}
    alist = []
    for i in range(len(path_list) - 1):
        curr_block, next_block = path_list[i:(i + 2)]
        alist.append(action_trans[next_block - curr_block])

    return alist
 # 状态转移函数，需要返回本次动作是否到达终点，本次动作的reward，本次动作后的下一个state
def Reward_state_action(s, a):
    # 向上移动
    if a == 0:
    # Fill and submit this code

    # 向下移动
    elif a == 1:
    # Fill and submit this code

    # 向左移动
    elif a == 2:
    # Fill and submit this code

    # 向右移动
    else:
    # Fill and submit this code

def epsilon_greedy(qtem, s, epsilon):
    # -------------------------------------
    # epsilon_greedy, 用于采样实现的动作选择
    # -------------------------------------
    return action

# on policy 基于epsilon-greedy策略进行num次实验，每次实验包含一个完整的episode，再根据episode进行策略改进
def Monte_Carlo(num, epsilon, gamma):
    # -------------------------------------
    # 定义状态-动作 函数qfunc (Q[s,a])并初始化
    # 定义Nqfunc统计某次episode中（s,a）出现的次数
    # 定义一个实验状态-动作函数qtem用于在采样实验中尽行动作的选择
        # 进行num次循环
            # 采用epsilon-greedy策略进行第K次episode采样实验
            # 定义三个数组用于存储第K次episode采样实验的states,actions,reward序列
            # 随机选择初始位置
            # 标记是否到达终点
            # 基于epsilon-greedy策略选择动作并执行动作
            # 行动完成后返回：
                # 这次行动是否到达终点
                # 这次行动后到达了哪一个状态
                # 这次行动获得的奖励
            # 更新实验的轨迹直到得到完整过程（起始位置->终止为止）的序列

            # 针对刚才生成的一幕完整的实验episode，进行策略改进
            # 定义并初始化回报值 g
            # 计算采样序列的起始状态回报值 g
                # 反向遍历采样到的序列，进行计算
            # 正向遍历采样到的序列当中的每一个状态-动作对，并更新qfunc
                # 把新的s-a的回报g和旧的qfunc[s,a]的回报，一起重新计算，求得更新后的 qfunc[s,a]
                # 需要注意每次计算时都需要更新g，以对应下一个状态
        # num次循环后得到最终的qfunc
    # -------------------------------------
    return qfunc

#根据最终的qfunc得到最优路径
def get_shortest_path(qfunc):
    # -------------------------------------
    # 根据最终得到的qfunc输出最优的路径
    # -------------------------------------
    return s_path

# Create default Malmo objects:
agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse(sys.argv)
except RuntimeError as e:
    print('ERROR:', e)
    print(agent_host.getUsage())
    exit(1)
if agent_host.receivedArgument("help"):
    print(agent_host.getUsage())
    exit(0)

if agent_host.receivedArgument("test"):
    num_repeats = 1
else:
    num_repeats = 5

for i in range(num_repeats):
    size = int(5)
    print("Size of maze:", size)
    my_mission = MalmoPython.MissionSpec(GetMissionXML("0", 0.4 + float(i / 20.0), size), True)
    my_mission_record = MalmoPython.MissionRecordSpec()
    my_mission.requestVideo(800, 500)
    my_mission.setViewpoint(1)
    # Attempt to start a mission:
    max_retries = 3
    my_clients = MalmoPython.ClientPool()
    my_clients.add(MalmoPython.ClientInfo('127.0.0.1', 10000))  # add Minecraft machines here as available

    for retry in range(max_retries):
        try:
            agent_host.startMission(my_mission, my_clients, my_mission_record, 0, "%s-%d" % ('Moshe', i))
            break
        except RuntimeError as e:
            if retry == max_retries - 1:
                print("Error starting mission", (i + 1), ":", e)
                exit(1)
            else:
                time.sleep(2)

    # Loop until mission starts:
    print("Waiting for the mission", (i + 1), "to start ", )
    world_state = agent_host.getWorldState()
    while not world_state.has_mission_begun:
        # sys.stdout.write(".")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print("Error:", error.text)

    print()
    print("Mission", (i + 1), "running.")

    grid = load_grid(world_state)
    start, end = find_start_end(grid)
    states = []   # 为简化计算可以仅获取迷宫中agent可站立的states
    actions = []  # 定义actions
    num =         #定义采样次数
    epsilon=      #定义epsilon
    gamma=        #定义gamma
    q=Monte_Carlo(num, epsilon, gamma)
    path = get_shortest_path(q)
    action_list=extract_action_list_from_path(path)

    print("Output (start,end)", (i + 1), ":", (start, end))
    print("Output (path length)", (i + 1), ":", len(path))
    print("Output (actions)", (i + 1), ":", action_list)
    # Loop until mission ends:
    action_index = 0
    while world_state.is_mission_running:
        # sys.stdout.write(".")
        time.sleep(0.1)

        # Sending the next commend from the action list -- found using the Dijkstra algo.
        if action_index >= len(action_list):
            print("Error:", "out of actions, but mission has not ended!")
            time.sleep(2)
        else:
            agent_host.sendCommand(action_list[action_index])
        action_index += 1
        if len(action_list) == action_index:
            # Need to wait few seconds to let the world state realise I'm in end block.
            # Another option could be just to add no move actions -- I thought sleep is more elegant.
            time.sleep(2)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print("Error:", error.text)

    print()
    print("Mission", (i + 1), "ended")
    # Mission has ended.
