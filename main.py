import streamlit as st

st.title('GPT')
st.markdown('Reference: _https://yaofu.notion.site/GPT-3-5-360081d91ec245f29029d37b54573756_')


st.header("GPT series model")
st.markdown('In Jul 2020. OpenAI released the initial GPT-3 paper with the davinci model index, and it started to evolve.')
st.markdown('***GPT-3.5*** series is a series of models that was trained on a blend of text and code from before Q4 2021.')
 

st.image("instr-tuning/路线.png", caption='GPT Model Evolutionary Tree')

st.header("Large Language Models Emergent Abilities")
st.markdown('There are three important abilities that the initial GPT-3 exhibit: ***Language generation, World knowledge, In-context learning***')


st.image("instr-tuning/能力.png", caption='GPT Model Abilities')

st.subheader("Where do these abilities come from?")
st.success('***Already be in the base model***: The ability to follow instruction and zero-shot generalization', icon="✅")
st.success('***Injected from code data during the pretraining stage***: The ability of complex reasoning', icon="✅")

st.markdown('• ***_Respond to human instructions_***: a direct product of instruction tuning')
st.markdown('• ***_Generalization to unseen instructions_***: a product of instruction tuning by scaling types of instructions')
st.markdown('• ***_Complex reasoning with chain-of-thought_***: a magical side product of training on code')
st.markdown('Note: _there is still no hard evidence showing training on code is absolutely the reason for CoT and complex reasoning_')


st.header("InstructGPT")

st.warning('Supervised instruction tuning', icon="🔥")
st.warning('Reinforcement learning from human feedback (RLHF)', icon="🔥")

st.subheader("The abilities triggered by RLHF")
st.markdown('• ***Informative responses***: text-davinci-003 的生成通常比 text-davinci-002长')
st.markdown('• ***Impartial responses***: 涉及多个实体利益的事件给出非常平衡的回答')
st.markdown('• ***Rejecting improper questions***: 内容过滤器和由 RLHF 触发的模型自身能力的结合')
st.markdown('• ***Rejecting questions outside its knowledge scope***: 使模型能够隐式地区分哪些问题在其知识范围内')

st.image("instr-tuning/InstructGPT.png", caption='GPT Model Abilities')







