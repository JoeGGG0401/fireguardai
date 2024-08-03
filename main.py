import time

import streamlit as st
import streamlit.components.v1 as components
import numpy as np

# 设置页面标题和副标题
st.set_page_config(page_title="FireGuard AI", page_icon="🧯", layout="wide")

# 创建侧边栏菜单
st.sidebar.title("操作菜单")
menu = st.sidebar.radio("选择操作", ["实时监控", "消防演练", "智能助手", "演练评估", "智能流程"])

# 初始化会话状态变量
if 'proceed' not in st.session_state:
    st.session_state.proceed = False

def realtime_monitoring():
    st.subheader("实时监控数据展示")

    # 系统状态选择和模拟设置
    status_options = ["正常", "预警", "火灾"]
    col1, col2 = st.columns([3, 1])

    with col2:
        status = st.selectbox("系统状态模拟设置", status_options)
    with col1:
        if status == "正常":
            st.markdown("### 当前系统状态: <span style='color: green;'>正常</span>", unsafe_allow_html=True)
            st.success("系统运行正常")
        elif status == "预警":
            st.markdown("### 当前系统状态: <span style='color: orange;'>预警</span>", unsafe_allow_html=True)
            st.warning("系统处于预警状态")
        else:  # 火灾状态
            st.markdown("### 当前系统状态: <span style='color: red;'>火灾</span>", unsafe_allow_html=True)
            st.error("系统处于火灾状态")

    # 根据系统状态设置数据
    if status == "正常":
        smoke_data = np.random.uniform(10, 30, 10)
        explosion_data = np.random.uniform(5, 15, 10)
        fire_spread_data = np.random.uniform(1, 5, 10)
        temperature_data = np.random.uniform(20, 25, 10)
        humidity_data = np.random.uniform(40, 60, 10)
    elif status == "预警":
        smoke_data = np.random.uniform(30, 60, 10)
        explosion_data = np.random.uniform(15, 30, 10)
        fire_spread_data = np.random.uniform(5, 10, 10)
        temperature_data = np.random.uniform(25, 30, 10)
        humidity_data = np.random.uniform(30, 50, 10)
    else:  # 火灾状态
        smoke_data = np.random.uniform(60, 100, 10)
        explosion_data = np.random.uniform(30, 50, 10)
        fire_spread_data = np.random.uniform(10, 20, 10)
        temperature_data = np.random.uniform(30, 40, 10)
        humidity_data = np.random.uniform(20, 40, 10)

    # 使用仪表盘和图表展示不同数据
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("烟雾浓度", f"{smoke_data[-1]:.2f}", delta=f"{smoke_data[-1] - smoke_data[-2]:.2f}")
    with col2:
        st.metric("爆燃指数", f"{explosion_data[-1]:.2f}", delta=f"{explosion_data[-1] - explosion_data[-2]:.2f}")
    with col3:
        st.metric("火势蔓延速度", f"{fire_spread_data[-1]:.2f}",
                  delta=f"{fire_spread_data[-1] - fire_spread_data[-2]:.2f}")

    col4, col5 = st.columns(2)
    with col4:
        st.metric("温度", f"{temperature_data[-1]:.2f}°C", delta=f"{temperature_data[-1] - temperature_data[-2]:.2f}°C")
        st.line_chart(temperature_data, width=300, height=200)
    with col5:
        st.metric("湿度", f"{humidity_data[-1]:.2f}%", delta=f"{humidity_data[-1] - humidity_data[-2]:.2f}%")
        st.line_chart(humidity_data, width=300, height=200)

    # 显示历史火灾演练结果摘要
    st.subheader("历史火灾演练结果摘要")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"#### 演练 1")
        with st.expander(f"演练 1 详情"):
            st.write(f"日期: 2024-01-15")
            st.write("结果：成功")
            st.write("响应时间：5分钟")
            st.write("人员疏散率：100%")
    with col2:
        st.markdown(f"#### 演练 2")
        with st.expander(f"演练 2 详情"):
            st.write(f"日期: 2024-02-15")
            st.write("结果：成功")
            st.write("响应时间：5分钟")
            st.write("人员疏散率：100%")
    with col3:
        st.markdown(f"#### 演练 3")
        with st.expander(f"演练 3 详情"):
            st.write(f"日期: 2024-03-15")
            st.write("结果：成功")
            st.write("响应时间：5分钟")
            st.write("人员疏散率：100%")


def fire_drill():
    st.subheader("消防演练")

    # 一键触发按钮
    if st.button("一键触发消防演练"):
        st.write("消防演练已触发")
        st.image("智能化流程.png", caption="自动化流程运行中")

        with st.spinner('模拟消防演练流程，请稍候...'):
            time.sleep(2)

            # 步骤 1: 获取监控信息
            st.write("**步骤 1: 获取监控信息**")
            st.write("获取“消防实时监控系统”的信息和“机房监控系统”的监控链接...")
            st.write("- 烟雾浓度: 45.3")
            st.write("- 爆燃指数: 3.2")
            st.write("- 火势蔓延速度: 0.8")
            monitoring_video_file = open("机房监控系统.mp4", "rb")
            monitoring_video_bytes = monitoring_video_file.read()
            st.video(monitoring_video_bytes)
            time.sleep(2)

            # 步骤 2: 预警审批
            approval = st.radio("是否确认继续演练？", ("确认", "否决"))
            if approval == "确认":
                st.session_state.proceed = True
                st.write("预警确认，继续演练...")
                time.sleep(2)
            else:
                st.session_state.proceed = False
                st.write("警报误触，已结束演练")

            if st.session_state.proceed == True:
                continue_fire_drill()


def continue_fire_drill():
    # 步骤 3: 发送通知
    st.write("**步骤 3: 发送通知**")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.image("预警群发消息.png", caption="群发预警通知")
    with col2:
        st.image("安保通知.png", caption="安保通知")
    st.image("消防报警.png", caption="消防报警")
    st.write("通知已发送。")
    time.sleep(2)

    # 步骤 4: 生成并发送疏散路线图
    st.write("**步骤 4: 生成并发送疏散路线图**")
    route_map_file = open("逃生路线.mp4", "rb")
    route_map_bytes = route_map_file.read()
    st.video(route_map_bytes)
    st.write("疏散路线图已发送。")
    time.sleep(2)

    # 步骤 5: 机房监控智能识别和灭火操作
    st.write("**步骤 5: 机房监控智能识别和灭火操作**")
    st.write("获取机房监控系统的监控链接...")
    monitoring_video_file = open("机房监控系统.mp4", "rb")
    monitoring_video_bytes = monitoring_video_file.read()
    st.video(monitoring_video_bytes)
    st.write("进行智能识别...")
    st.image("机房监控智能识别.png", caption="智能识别中")
    time.sleep(2)
    st.write("开始灭火操作...")
    fire_extinguishing_operation_file = open("灭火视频.mp4", "rb")
    fire_extinguishing_operation_bytes = fire_extinguishing_operation_file.read()
    st.video(fire_extinguishing_operation_bytes)
    st.write("灭火操作在园区屏幕上播放中。")
    time.sleep(2)

    # 步骤 6: 生成并发送事故单
    st.write("**步骤 6: 生成并发送事故单**")
    with open('火警火灾事故报告表.docx', 'rb') as incident_ticket_file:
        st.download_button('下载事故单', incident_ticket_file, '火警火灾事故报告表.docx')
    st.image("事故单发送.png", caption="事故单发送")
    st.write("事故单已生成并发送至相关部门。")

def evaluation():
    st.subheader("演练评估")

    # 数据分析
    st.write("数据分析结果：")
    data = np.random.randn(10, 3)
    st.bar_chart(data)

    # 报告生成
    st.write("演练报告：已生成")
    file_path = "演练报告.docx"

    with open(file_path, "rb") as file:
        st.download_button(
            label="下载报告",
            data=file,
            file_name="演练报告.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )


# 定义演练评估页面

def intelligent_workflow():
    intelligent_workflow_file = open("智能化流程.mp4", "rb")
    intelligent_workflow_bytes = intelligent_workflow_file.read()
    st.video(intelligent_workflow_bytes)

    st.markdown("""
    ### 智能化流程

    在当今快速发展的商业环境中，企业面临着不断变化的需求和复杂的操作流程。为了帮助企业高效应对这些挑战，我们推出了全新的智能化流程管理解决方案。我们的特色在于流程的内部智能化和搭建流程的智能化，解决了业务人员上手流程工具难度大的痛点，同时也显著提高了团队协作效率。

    #### 智能化流程的核心特色：

    1. **流程内部智能化**
       - **自动化处理**：我们的系统能够自动识别并处理流程中的关键节点，减少人为干预，提升整体效率。
       - **实时监控与反馈**：系统实时监控流程执行情况，并在异常情况发生时提供即时反馈，确保流程顺利进行。
       - **数据驱动决策**：通过对流程数据的智能分析，提供优化建议，帮助企业持续改进流程。

    2. **智能化搭建流程**
       - **用户友好界面**：直观的拖拽式界面，让业务人员无需编程知识即可轻松搭建复杂的业务流程。
       - **智能推荐**：基于历史数据和最佳实践，系统智能推荐适合的流程模板，帮助快速搭建和优化流程。
       - **自定义灵活性**：支持用户根据具体需求进行流程定制，确保流程能够精准匹配业务需求。

    3. **高效协作**
       - **跨部门协作**：通过共享工作流模板，各部门之间可以快速共享和微调流程，实现高效协作。
       - **版本控制与权限管理**：支持多版本流程管理和细粒度权限控制，确保流程在协作中的安全和一致性。
       - **沟通与反馈机制**：内置的沟通和反馈机制，确保团队成员能够及时交流和解决问题。

    4. **系统集成**
       - **无缝适配现有系统**：支持与现有的ERP、CRM等系统无缝集成，避免重复建设和数据孤岛现象。
       - **标准化接口**：提供标准化API接口，方便系统间的数据交互和功能扩展。
       - **工具介入支持**：支持各种第三方工具的介入，进一步提升流程的灵活性和可扩展性。

    通过我们的智能化流程管理解决方案，企业不仅能够快速搭建和优化业务流程，还能显著提升团队的协作效率和整体运营水平。无论是初创企业还是大型企业，都能从中受益，实现业务的智能化和高效化。
    """)


# Define the Intelligent Assistant page
def intelligent_assistant():
    components.iframe("http://dify.laplacelab.ai/chat/6tpjrESm0KSihET0", height=650)


# 根据菜单选择显示不同页面
if menu == "实时监控":
    realtime_monitoring()
elif menu == "消防演练":
    fire_drill()
elif menu == "智能助手":
    intelligent_assistant()
elif menu == "演练评估":
    evaluation()
else:
    intelligent_workflow()