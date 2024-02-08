<?php
<?php
flush();
ob_start();
set_time_limit(0);
error_reporting(0);
ob_implicit_flush(1);

$token = "6353045233:AAErQdiPPx4NJBJioHgnyEyJGuuoBlRofck";

define('API_KEY',$token);
echo "setWebhook ~> <a href=\"https://api.telegram.org/bot".API_KEY."/setwebhook?url=".$_SERVER['SERVER_NAME']."".$_SERVER['SCRIPT_NAME']."\">https://api.telegram.org/bot".API_KEY."/setwebhook?url=".$_SERVER['SERVER_NAME']."".$_SERVER['SCRIPT_NAME']."</a>";
function bot($method,$datas=[]){
$url = "https://api.telegram.org/bot".API_KEY."/".$method;
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,$url); curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
$res = curl_exec($ch);
if(curl_error($ch)){
var_dump(curl_error($ch));
}else{
return json_decode($res);
}}

#Short
$update = json_decode(file_get_contents("php://input"));
file_put_contents("update.txt",json_encode($update));
$message = $update->message;
$txt = $message->caption;
$text = $message->text;
$chat_id = $message->chat->id;
$from_id = $message->from->id;
$new = $message->new_chat_members;
$message_id = $message->message_id;
$type = $message->chat->type;
$name = $message->from->first_name;
$typen = $message->chat->type;
$from_id = $message->from->id;
$forward =$message->forward_from_chat;
$forwardid = $message->forward_from_chat->id;
$text = $message->text;
$id = $message->from->id;
$caption = $update->message->caption;
$message_id = $message->message_id;
$t =$message->chat->title; 
if(isset($update->callback_query)){
$up = $update->callback_query;
$chat_id = $up->message->chat->id;
$from_id = $up->from->id;
$user = $up->from->username;
$name = $up->from->first_name;
$message_id = $up->message->message_id;
$data = $up->data;
}
if(isset($update->channel_post)){
 $chat_id = $update->channel_post->chat->id;
 $message_id = $update->channel_post->message_id;
 $message = $update->channel_post;
 $text = $update->channel_post->text;
 $textpost = $update->channel_post->text;
 if
($update->channel_post->message->caption) {
$caption = $update->channel_post->message->caption;
}}
  
#$id = $update->inline_query->from->id; 
$admin = "00";
$sudo = array("$absdev","00"); #ايديات الادمنيةه
$idbot = "6353045233"; #
$userbot = "@Mmagnnonbot"; #يوزر البوت
$userbots = "@$userbot";
$buy = "@R_M171"; #معرفك
$chi = "https://@almooorrth"; #معرف قناتك
mkdir("sudo");
mkdir("data");

$member = explode("\n",file_get_contents("sudo/member.txt"));
$cunte = count($member)-1;
$ban = explode("\n",file_get_contents("sudo/ban.txt"));
$countban = count($ban);

$admins=explode("\n",file_get_contents("sudo/admin.txt"));#الادمنية
$member = explode("\n",file_get_contents("sudo/member.txt"));
$cunte = count($member)-1;
$members = file_get_contents("sudo/member.txt");#تخزين الاعضاء
$groups = file_get_contents("sudo/groups.txt");#تخزين القروبات
$ex_groups = explode("\n",$groups);
$countgroups = count($ex_groups)-1;
$channels = file_get_contents("sudo/channels.txt");#تخزين القنوات
$ex_channels = explode("\n",$channels);
$countchannels = count($ex_channels)-1;

if ($text == '/start' ){
if(!in_array($from_id,$sudo)){
  bot('sendMessage', [
  'chat_id' => $chat_id, 
  'text' => "
لايمكن استخدام البوت في ادارة المنشورات لغير المالك للبوت 

$txtfree",
 'parse_mode'=>"html",
 'disable_web_page_preview' => true,]);
  
  }}

$infodata = json_decode(file_get_contents("data/data.json"),true);
if (!file_exists("data/data.json")) {
#	$put = [];

$infodata["info"]["namech"]="معطل";
$infodata["info"]["likech"]="معطل";
$infodata["info"]["talig"]="معطل";
$infodata["info"]["hogog"]="معطل";

$infodata["info"]["fwrch"]="معطل";
$infodata["info"]["delhg"]="معطل";
$infodata["info"]["msabgat"]="معطل";


file_put_contents("data/data.json", json_encode($infodata));
}


$namech=$infodata["info"]["namech"];
$likech=$infodata["info"]["likech"];
$t3lig=$infodata["info"]["talig"];
$hogog=$infodata["info"]["hogog"];
$fwrch=$infodata["info"]["fwrch"];
$delhg=$infodata["info"]["delhg"];
$msabgat=$infodata["info"]["msabgat"];



if($text == "/start" and in_array($from_id,$sudo)){

bot('sendmessage',[
'chat_id'=>$chat_id, 
'text'=>"
• اهلا بك عزيزي - $name 🔱 •

 في بوت ادارة منشورات القناة الخاص بك 

• عليك اولا رفع البوت ادمن في قناتك
- البوت يعمل عند نشر منشور جديد في القناة 
 
• يمكنك اضافه زر لايك ودس لايك تلقائيا في قناتك 
• يمكنك اضافه زر يحتوي على اسم القناة ورابط القناة 
• يمكنك اضافه زر اضف تعليق ورد على تعليقات 
• يمكنك وضع حقوق في نهايه كل منشور ( نصوص او ميديا )
• يمكنك تفعيل مسح الحقوق الموجوده في المنشورات مثل روابط و المعرفات 
• يمكنك تفعيل خاصيه اعاده نشر الرسائل الموجهة ( نصوص او ميديا )

- يمكنك التحكم بواسطه الازرار ❤️
 ",
'parse_mode'=>markdown,
'disable_web_page_preview'=>true,
"message_id"=>$message_id,
'reply_markup'=>json_encode(['inline_keyboard'=>[

[['text'=>"زر اسم + رابط القناة : $namech ",'callback_data'=>"namech"]],[['text'=>"زر الايك + ديسكلايك :$likech",'callback_data'=>"likech"]],
[['text'=>"زر اضف تعليق : $t3lig",'callback_data'=>"talig"]],
[['text'=>" اضف حقوق : $hogog",'callback_data'=>"hogog"]],
[['text'=>"إعادة نشر التوجية : $fwrch",'callback_data'=>"fwrch"]],
[['text'=>" مسح الحقوق : $delhg",'callback_data'=>"delhg"]],
[['text'=>" وضع المسابقات : $msabgat",'callback_data'=>"msabgat"]],
]
])
]);
}

function sendwataw3($chat_id,$message_id){
$infodata = json_decode(file_get_contents("data/data.json"),true);
$namech=$infodata["info"]["namech"];
$likech=$infodata["info"]["likech"];
$t3lig=$infodata["info"]["talig"];
$hogog=$infodata["info"]["hogog"];
$fwrch=$infodata["info"]["fwrch"];
$delhg=$infodata["info"]["delhg"];
$msabgat=$infodata["info"]["msabgat"];
bot('EditMessageText',[
'chat_id'=>$chat_id, 
'text'=>"• اهلا بك عزيزي - $name 🔱 •

 في بوت ادارة منشورات القناة الخاص بك 

• عليك اولا رفع البوت ادمن في قناتك
- البوت يعمل عند نشر منشور جديد في القناة 
 
• يمكنك اضافه زر لايك ودس لايك تلقائيا في قناتك 
• يمكنك اضافه زر يحتوي على اسم القناة ورابط القناة 
• يمكنك اضافه زر اضف تعليق ورد على تعليقات 
• يمكنك وضع حقوق في نهايه كل منشور ( نصوص او ميديا )
• يمكنك تفعيل مسح الحقوق الموجوده في المنشورات مثل روابط و المعرفات 
• يمكنك تفعيل خاصيه اعاده نشر الرسائل الموجهة ( نصوص او ميديا )

- يمكنك التحكم بواسطه الازرار ❤️
",
'parse_mode'=>markdown,
'disable_web_page_preview'=>true,
"message_id"=>$message_id,
'reply_markup'=>json_encode(['inline_keyboard'=>[

[['text'=>"زر اسم + رابط القناة : $namech ",'callback_data'=>"namech"]],[['text'=>"زر الايك + ديسكلايك :$likech",'callback_data'=>"likech"]],
[['text'=>"زر اضف تعليق : $t3lig",'callback_data'=>"talig"]],
[['text'=>" اضف حقوق : $hogog",'callback_data'=>"hogog"]],
[['text'=>"إعادة نشر التوجية : $fwrch",'callback_data'=>"fwrch"]],
[['text'=>" مسح الحقوق : $delhg",'callback_data'=>"delhg"]],
[['text'=>" وضع المسابقات : $msabgat",'callback_data'=>"msabgat"]],
]
])
]);
} 

if($data == "hogog" and in_array($from_id,$sudo)){

$infodata = json_decode(file_get_contents("data/data.json"),true);
$hogog=$infodata["info"]["hogog"];
if($hogog=="مفعل"){
$infodata["info"]["hogog"]="معطل";
}
if($hogog=="معطل"){
$infodata["info"]["hogog"]="مفعل";
}
file_put_contents("data/data.json", json_encode($infodata));

}
if($data == "hogog" and in_array($from_id,$sudo)){

$infosudo["info"]["amr"]="hogog";
file_put_contents("sudo.json", json_encode($infosudo));
bot('EditMessageText',[
'chat_id'=>$chat_id, 
'text'=>"- قم بإرسال الحقوق
",
'parse_mode'=>markdown,
'disable_web_page_preview'=>true,
"message_id"=>$message_id,
'reply_markup'=>json_encode(['inline_keyboard'=>[

[['text'=>"- الغاء  ",'callback_data'=>"home2"]],
]
])
]);

}

if($text  and $text !="/start" and $infosudo["info"]["amr"]=="hogog" and in_array($from_id,$sudo)){
bot('sendmessage',[
'chat_id'=>$chat_id, 
'text'=>"- ✅ تم حفظ الحقوق بنجاح
-الحقوق : 
$text ",
'disable_web_page_preview'=>true,
"message_id"=>$message_id,
'reply_markup'=>json_encode(['inline_keyboard'=>[

[['text'=>"- عودة  ",'callback_data'=>"home2"]],
]
])
]);
$infosudo["info"]["amr"]="null";

file_put_contents("sudo.json", json_encode($infosudo));

$infodata["info"]["klish_hogog"]="$text";

file_put_contents("data/data.json", json_encode($infodata));



}
if($data == "home2"){
$infosudo["info"]["amr"]="null";
file_put_contents("sudo.json", json_encode($infosudo));
sendwataw3($chat_id,$message_id);
}
#name

if($data == "namech"){
$infodata = json_decode(file_get_contents("data/data.json"),true);
$namech=$infodata["info"]["namech"];
if($namech=="مفعل"){
$infodata["info"]["namech"]="معطل";
}
if($namech=="معطل"){
$infodata["info"]["namech"]="مفعل";
}
file_put_contents("data/data.json", json_encode($infodata));
sendwataw3($chat_id,$message_id);
}

#like

if($data == "likech"){
$infodata = json_decode(file_get_contents("data/data.json"),true);
$likech=$infodata["info"]["likech"];
if($likech=="مفعل"){
$infodata["info"]["likech"]="معطل";
}
if($likech=="معطل"){
$infodata["info"]["likech"]="مفعل";
}
file_put_contents("data/data.json", json_encode($infodata));
sendwataw3($chat_id,$message_id);
}
#talig
if($data == "talig"){
$infodata = json_decode(file_get_contents("data/data.json"),true);
$talig=$infodata["info"]["talig"];
if($t3lig=="مفعل"){
$infodata["info"]["talig"]="معطل";
}
if($t3lig=="معطل"){
$infodata["info"]["talig"]="مفعل";
}
file_put_contents("data/data.json", json_encode($infodata));
sendwataw3($chat_id,$message_id);
}
#fwrch
if($data == "fwrch"){
$infodata = json_decode(file_get_contents("data/data.json"),true);
$join=$infodata["info"]["fwrch"];
if($join=="مفعل"){
$infodata["info"]["fwrch"]="معطل";
}
if($join=="معطل"){
$infodata["info"]["fwrch"]="مفعل";
}
file_put_contents("data/data.json", json_encode($infodata));
sendwataw3($chat_id,$message_id);
}
#delhg
if($data == "delhg"){
$infodata = json_decode(file_get_contents("data/data.json"),true);
$join=$infodata["info"]["delhg"];
if($join=="مفعل"){
$infodata["info"]["delhg"]="معطل";
}
if($join=="معطل"){
$infodata["info"]["delhg"]="مفعل";
}
file_put_contents("data/data.json", json_encode($infodata));
sendwataw3($chat_id,$message_id);
}
#msabgat
if($data == "msabgat"){
$infodata = json_decode(file_get_contents("data/data.json"),true);
$join=$infodata["info"]["msabgat"];
if($join=="مفعل"){
$infodata["info"]["msabgat"]="معطل";
}
if($join=="معطل"){
$infodata["info"]["msabgat"]="مفعل";
}
file_put_contents("data/data.json", json_encode($infodata));
sendwataw3($chat_id,$message_id);
}


$title = $update->channel_post->chat->title;
$user_channel = $update->channel_post->chat->username;
$Caption= $update->channel_post->Caption;
$channel_id = $update->channel_post->chat->id;
$channeltext= $update->channel_post->text;
$channel_message_id= $update->channel_post->message_id;


$namech=$infodata["info"]["namech"];
$likech=$infodata["info"]["likech"];
$t3lig=$infodata["info"]["talig"];
$hogog=$infodata["info"]["hogog"];
$fwrch=$infodata["info"]["fwrch"];
$delhg=$infodata["info"]["delhg"];
$msabgat=$infodata["info"]["msabgat"];
$klish_hogog=$infodata["info"]["klish_hogog"];

$msgs = json_decode(file_get_contents("data/mesg.json"),true);

if (!file_exists("data/mesg.json")) {
    $msgs = array();
    file_put_contents("data/mesg.json", json_encode($msgs));
}

$like = json_decode(file_get_contents("data/like.json"),true);

if (!file_exists("data/like.json")) {
    $like = array();
    file_put_contents("data/like.json", json_encode($like));
}


if($update->channel_post and !$forward){
if($msabgat=="مفعل"){
$msgs["info"][$channel_id][$channel_message_id]["love"]["stats"]="yes";
$msgs["info"][$channel_id][$channel_message_id]["love"]="yes";
$keyboard["inline_keyboard"][] =
[['text'=>'📂 ','callback_data'=>'like love']];
}
if($likech=="مفعل"){
$msgs["info"][$channel_id][$channel_message_id]["like"]="yes";
$keyboard["inline_keyboard"][] =
[['text'=>'👍','callback_data'=>'like like'],['text'=>'👎','callback_data'=>'like nolike']];
}
if($t3lig=="مفعل"){
$msgs["info"][$channel_id][$channel_message_id]["t3lig"]="yes";
$keyboard["inline_keyboard"][] =
[['text'=>'إرسال تعليق','url'=>"https://t.me/$userbot?start=t3lig&$channel_id&$channel_message_id&$user_channel"]];
}
if($namech=="مفعل"){
$msgs["info"][$channel_id][$channel_message_id]["namech"]="yes";
$keyboard["inline_keyboard"][] =
[['text'=>$title,'url'=>'https://t.me/'.$user_channel]];
}
$reply_markup=json_encode($keyboard);





if($channeltext){
$txt=$channeltext;
if($hogog=="مفعل"){
$txt=$channeltext."\n\n".$klish_hogog;
}
bot('EditMessageText',[
'chat_id'=>$channel_id, 
'text'=>"$txt
",

'disable_web_page_preview'=>true,
"message_id"=>$channel_message_id,
'reply_markup'=>$reply_markup
]);
}else{
$txt=$Caption;
if($hogog=="مفعل"){
$txt=$Caption."\n\n".$klish_hogog;
}
bot('editMessageCaption',[
'chat_id'=>$channel_id, 
'caption'=>"$txt
",
'disable_web_page_preview'=>true,
"message_id"=>$channel_message_id,
'reply_markup'=>$reply_markup
]);
}
file_put_contents("data/mesg.json", json_encode($msgs));

}




$msg_inline   = $update->callback_query->inline_message_id;

$love=$msgs["info"][$chat_id][$message_id]["love"];

$likkch=$msgs["info"][$chat_id][$message_id]["like"];
$t3liglike=$msgs["info"][$chat_id][$message_id]["t3lig"];
$namechlike=$msgs["info"][$chat_id][$message_id]["namech"];

if(preg_match('/^(like) (.*)/s', $data)){
$nn = str_replace('like ',"",$data);
#$ex=explode(':',$nn);
$am=$nn;
#$co=$ex[1];
$like = json_decode(file_get_contents("data/like.json"),true);
$arraylike=$like["info"][$chat_id][$message_id]["member"];
if(!in_array($from_id,$arraylike)){
$keyboard["inline_keyboard"]=[];
$colove=$like["info"][$chat_id][$message_id]["love"];
$colike=$like["info"][$chat_id][$message_id]["like"];
$conolike=$like["info"][$chat_id][$message_id]["nolike"];
if($am=='love'){
$colove=$colove+1;
}
if($love=="yes"){
$keyboard["inline_keyboard"][] =
[['text'=>'📂 '.$colove,'callback_data'=>'like love']];
}
if($am=='like'){
$colike=$colike+1;
}
if($am=='nolike'){
$conolike=$conolike+1;

}
if($likkch=="yes"){
$keyboard["inline_keyboard"][] =
[['text'=>'👍'.$colike,'callback_data'=>'like like'],['text'=>'👎'.$conolike,'callback_data'=>'like nolike']];
}

if($t3liglike=="yes"){
$keyboard["inline_keyboard"][] =
[['text'=>'إرسال تعليق','url'=>"https://t.me/$userbot?start=t3lig&$chat_id$message_id&".$update->callback_query->message->chat->username]];
}
if($namechlike=="yes"){
$keyboard["inline_keyboard"][] =
[['text'=> $update->callback_query->message->chat->title,'url'=>'https://t.me/'.$update->callback_query->message->chat->username]];
}
$reply_markup=json_encode($keyboard);

bot('editMessageReplyMarkup',[
'chat_id'=>$chat_id,
		"message_id"=>$message_id,
			'reply_markup'=>$reply_markup

]);

$like["info"][$chat_id][$message_id]["love"]="$colove";
$like["info"][$chat_id][$message_id]["like"]="$colike";
$like["info"][$chat_id][$message_id]["nolike"]="$conolike";
$like["info"][$chat_id][$message_id]["member"][]="$from_id";
file_put_contents("data/like.json", json_encode($like));
bot('answerCallbackQuery',[
            'callback_query_id'=>$update->callback_query->id,
            'text'=>"✅ تم التصويت بنجاح
            
            ",
            'show_alert'=>true
            ]);
}else{
bot('answerCallbackQuery',[
            'callback_query_id'=>$update->callback_query->id,
            'text'=>"🚫 لايمكنك التصويت مرتين ",
            'show_alert'=>true
            ]);

}
}



$voice       = $update->channel_post->voice;
$document       = $update->channel_post->document;
    $sticker        = $update->channel_post->sticker;
    $photo          = $update->channel_post->photo;
    $video          = $update->channel_post->video;
    $forward        = $update->channel_post->forward_from_chat;
    $contact        = $update->channel_post->contact;
    $audio          = $update->channel_post->audio;
    $is_sticker = $update->channel_post->sticker->is_sticker;
    $video_note = $update->channel_post->video_note;

if($fwrch=="مفعل" and $forward ){

if($photo){
$sens="sendphoto";
$file_id = $update->channel_post->photo[1]->file_id;
}
if($document){
$sens="senddocument";
$file_id = $update->channel_post->document->file_id;
}
if($video){
$sens="sendvideo";
$file_id = $update->channel_post->video->file_id;
}

if($audio){
$sens="sendaudio";
$file_id = $update->channel_post->audio->file_id;
}

if($voice){
$sens="sendvoice";
$file_id = $update->channel_post->voice->file_id;
}

if($sticker){
$sens="sendsticker";
$file_id = $update->channel_post->sticker->file_id;
}

$st="yes";
}
if($st=="yes" and $fwrch=="مفعل" and $forward ){
bot('deletemessage', [
'chat_id'=>$channel_id,
'message_id'=>$channel_message_id,

]);
if($text){
bot('sendMessage', [
'chat_id'=>$channel_id,
'text'=>"$channeltext",
'disable_web_page_preview'=>true,
]);

}else{
$ss=str_replace("send","",$sens);
bot($sens,[
"chat_id"=>$channel_id,
"$ss"=>"$file_id",
'caption'=>"$Caption",
]);
}
}

$aaa=file_get_contents("data/$from_id.txt");


$txt = explode(' ', $text);
if (isset($txt[0]) and isset($txt[1]) and $txt[0]=='/start' and $txt[1] != null) {
$tx = explode('#', $text);
bot('ForwardMessage',[
 'chat_id'=>$chat_id,
 'from_chat_id'=>$tx[1],
 'message_id'=>$tx[2],
]);
file_put_contents("data/$from_id.txt","yes");
file_put_contents("data/$from_id-data.txt","$text");


    bot('sendMessage',[
        'chat_id'=>$chat_id,
        'text'=>'الان قم بأرسال تعليقك  📝',
        'reply_markup'=>json_encode([
                'inline_keyboard'=>[
                [['text'=>'خروج 🗳','callback_data'=>"out"]]
                ]])
        ]);
}

if($text and $aaa=="yes"){
$x=explode('&',file_get_contents("data/$from_id-data.txt"));

bot('sendMessage',[
        'chat_id'=>$absdev,
        'text'=>"لديك تعليق على منشور  


-التعليق : $text 
من : $name
",
        
        ]);

unlink("data/$from_id-data.txt");
unlink("data/$from_id.txt");
bot('sendMessage',[
        'chat_id'=>$chat_id,
        'text'=>'تم ارسال تعليقك بنجاح',
        
        ]);

}

if($data=="out"){

bot('sendMessage',[
        'chat_id'=>$chat_id,
        'text'=>"تم الغاء الارسال
",
        
        ]);

unlink("data/$from_id-data.txt");
unlink("data/$from_id.txt");


}





