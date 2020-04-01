<style lang="scss" scoped>

</style>

<template>
	<Row>
		<Col>
			<Row>
				<Col offset="7" span="10">
					<Row>
						<Col>
							<div style="text-align:center">
								<Upload
									:show-upload-list="false"
									:default-file-list="false"
									:format="['jpg','jpeg','png']"
									:max-size="2048"
									:on-success="uploadSuccess"
									:on-error="uploadError"
									:on-format-error="handleFormatError"
									:on-exceeded-size="handleMaxSize"
									:before-upload="handleBeforeUpload"
									multiple
									type="drag"
									action="http://127.0.0.1:8000/api/app_ocr/create-img/"
								>
									<div style="padding: 20px 0">
										<Icon type="ios-cloud-upload" size="52" style="color: #3399ff"></Icon>
										<p>Click or drag files here to upload</p>
									</div>
								</Upload>
								<Divider orientation="left">分割线</Divider>
							</div>
						</Col>
					</Row>
					<Row>
						<Col>
							<div class="demo-split" >
								<Split v-model="0.7" >
									<div slot="left" class="demo-split-pane" >
										<div v-for="image in this.image.base64_data" >
											<img v-bind:src="image" style="max-width: 100%;max-height: 200px">
											<Divider/>
										</div>
									</div>
									<div slot="right" class="demo-split-pane">
										<div v-for="keys in this.image.key_data" >
											<div v-for="key in keys" >
												{{key}}
											</div>
											<Divider/>
										</div>
									</div>
								</Split>
							</div>
						</Col>
					</Row>
				</Col>
			</Row>
		</Col>
	</Row>
</template>
<script>
    export default {
        data () {
            return {
                split1: 0.7,
                image:{}
            }
        },
        methods: {
            uploadSuccess (response, file, fileList) { // 文件上传成功时的钩子，返回字段为 response, file, fileList
                this.$Message.success("识别成功");
                console.log("response2:",response.results);
                this.$store.commit("update_current_image_data",response.results);
                this.image = this.$store.getters.get_current_image_detail;
            },
            uploadError(error, file, fileList){ // 文件上传失败时的钩子，返回字段为 error, file, fileList
                this.$Message.error("节流限制,每分钟最多3次提交");
            },
            handleFormatError(file, fileList){ // 文件格式验证失败时的钩子，返回字段为 file, fileList

            },
            handleMaxSize(file, fileList){ // 文件超出指定大小限制时的钩子，返回字段为 file, fileList

            },
            handleBeforeUpload(response){ // 上传文件之前的钩子，参数为上传的文件，若返回 false 或者 Promise 则停止上传

            }
        },
    }
</script>
<style>
	.demo-upload-list{
		display: inline-block;
		width: 60px;
		height: 60px;
		text-align: center;
		line-height: 60px;
		border: 1px solid transparent;
		border-radius: 4px;
		overflow: hidden;
		background: #fff;
		position: relative;
		box-shadow: 0 1px 1px rgba(0,0,0,.2);
		margin-right: 4px;
	}
	.demo-upload-list img{
		width: 100%;
		height: 100%;
	}
	.demo-upload-list-cover{
		display: none;
		position: absolute;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		background: rgba(0,0,0,.6);
	}
	.demo-upload-list:hover .demo-upload-list-cover{
		display: block;
	}
	.demo-upload-list-cover i{
		color: #fff;
		font-size: 20px;
		cursor: pointer;
		margin: 0 2px;
	}
	.demo-split{
		height: 1000px;
		border: 1px solid #dcdee2;
	}
	.demo-split-pane{
		padding: 10px;
	}
</style>






