# dangdang_project
当当网项目模型

1. 当当网的技术点划分
	a. 前端页面 + 后端程序 + 数据库开发
	b. 主要实现的是后端部分，数据库设计和前端页面的数据的渲染 -- 会提供前端页面给大家，我们只需要修改前端页面中需要展示数据的地方 -- {{模板语言}} {% for/if %}
	
2. 功能划分
	a. 首页展示
	b. 分类展示
	c. 书籍详情
	d. 购物车
	e. 订单
	f. 收货地址管理
	g. 登录注册 等
  
  
  3. 项目的基本开发流程
	(1) 需求分析
		-- 明确项目需要实现什么功能，不用关心怎么实现（具体实现） - PM
		-- 每天早上开需求分析会 - 项目经理、产品经理、程序员、UI设计人员.. 
	
	(2) 库表设计 
		-- 表先行
		-- 涉及到哪些数据
		-- 需要设计出哪些表
		-- 表与表之前有哪些关联
		-- 表里面有哪些字段
		-- 专业的工具来做库表设计 - Navicat 
			-- 之前：先定义model类，再迁移生成表
			-- 现在：先设计表，然后再根据表来生成model类 先有图纸再盖房子
		
	(3) 详细设计
		-- 每一块功能模块具体怎么做 
		-- 每天会给大家讲解每个模块的详细设计
	(4) 编码
		-- 让程序员夜以继日地去干，996 007 
	(5) 测试
		-- 程序员自测 - 很难找到bug 
		-- 测试人员测试项目，提交测试文档-bug，bug日清
		-- 黑盒测试/白盒测试  
		-- 写测试代码
	(6) 环境部署
		-- 购买云服务器，开发人员或运维做环境部署
	(7) 项目上线运行
		-- 开发人员或运维
	(8) 运维 / 运营 
    	-- 维护项目的日常运行（运维：背锅） 项目推广（运营：线上广告、地推）
    
4. 项目周期
	2周（包括周六日）
	
5. 开发形式
	前二/三天，小组协作，后面个人独立完成（每一个人完成一个当当网，与企业不同）
	
6. 项目验收
	-- 面试项目演示，无BUG或bug极少，没有大的bug影响项目运行
	-- 功能完整，符合最初的需求
	-- 知识点提问，做完项目后，知识点是否掌握，项目是否是自己独立完成的
