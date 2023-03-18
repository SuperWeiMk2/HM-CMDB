<template>
  <div class="repo-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>配置</n-breadcrumb-item>
          <n-breadcrumb-item>存储库</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-input v-model:value="repoName" style="width: 200px; margin-right: 10px; " type="text"
               placeholder="请输入名称"/>
      <n-select v-model:value="repoConnectTypeSelectOptionValue" :options="repoConnectTypeSelectOptions"
                style="width: 200px; margin-right: 10px;" placeholder="请选择类型"/>
      <n-input v-model:value="repoUsage" style="margin-right: 10px; " type="text"
               placeholder="请输入用途, 支持全文检索.."/>
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="info">
            <template #icon>
              <n-icon>
                <search-outlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>按照指定条件进行搜索</span>
      </n-tooltip>
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="success" @click="handleAddButtonClicked">
            <template #icon>
              <n-icon>
                <plus-outlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>添加</span>
      </n-tooltip>
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="warning"
                    @click="handleBatchDeleteButtonClicked">
            <template #icon>
              <n-icon>
                <delete-outlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>删除选中的条目</span>
      </n-tooltip>
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="error">
            <template #icon>
              <n-icon>
                <close-outlined/>
              </n-icon>
            </template>
          </n-button>
        </template>
        <span>清空搜索条件</span>
      </n-tooltip>
    </div>
    <n-data-table striped :columns="columns" :data="repos" :pagination="pagination"/>
    <n-modal v-model:show="isShowAddModal" :mask-closablef="false" preset="card" title="添加存储库"
             :on-after-leave="onAddModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">名称</div>
          <n-input v-model:value="createRepoName" type="text" placeholder="必填, 请输入名称" style="margin-bottom: 10px; max-width: 350px"/>
          <div style="font-size: 12pt; font-weight: bold;">类型</div>
          <n-select v-model:value="createRepoType" :options="repoConnectTypeSelectOptions" type="text" placeholder="必填, 请选择类型" style="margin-bottom: 10px; max-width: 150px"/>
          <div style="font-size: 12pt; font-weight: bold;">地址</div>
          <n-input v-model:value="createRepoAddress" type="text" placeholder="必填, 请输入地址" style="margin-bottom: 10px; max-width: 500px"/>
          <div style="font-size: 12pt; font-weight: bold;">用途</div>
          <n-input v-model:value="createRepoUsage" type="text" placeholder="必填, 请输入用途" style="margin-bottom: 10px;"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onAddModalFailed" style="margin-right: 10px;">取&nbsp;消</n-button>
          <n-button @click="onAddModalOk" type="primary">添&nbsp;加</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowDetailModal" :mask-closablef="false" preset="card" title="xxx的详情"
             :on-after-leave="onDetailModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">类型</div>
          <n-select type="text" placeholder="必填, 请选择类型" style="margin-bottom: 10px; max-width: 150px" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">地址</div>
          <n-input type="text" placeholder="必填, 请输入地址" style="margin-bottom: 10px; max-width: 500px" disabled/>
          <div style="font-size: 12pt; font-weight: bold;">用途</div>
          <n-input type="text" placeholder="必填, 请输入用途" style="margin-bottom: 10px;" disabled/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onDetailModalOk" type="primary">关&nbsp;闭</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowModifyModal" :mask-closablef="false" preset="card" title="修改存储库"
             :on-after-leave="onModifyModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">类型</div>
          <n-select v-model:value="updateByType" type="text" :options="repoConnectTypeSelectOptions" placeholder="必填, 请选择类型" style="margin-bottom: 10px; max-width: 150px"/>
          <div style="font-size: 12pt; font-weight: bold;">地址</div>
          <n-input v-model:value="updateByAddress" type="text" placeholder="必填, 请输入地址" style="margin-bottom: 10px; max-width: 500px"/>
          <div style="font-size: 12pt; font-weight: bold;">用途</div>
          <n-input v-model:value="updateByUsage" type="text" placeholder="必填, 请输入用途" style="margin-bottom: 10px;"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onModifyModalFailed" style="margin-right: 10px;">取&nbsp;消</n-button>
          <n-button @click="onModifyModalOk" type="primary">修&nbsp;改</n-button>
        </div>
      </div>
    </n-modal>
    <div style="width: 100%; min-height: 20px;"></div>
  </div>
</template>

<script setup>
import {getCurrentInstance, h, onMounted, reactive, ref} from "vue";
import {NButton, NTag, useDialog, useMessage} from "naive-ui";
import {SearchOutlined, CloseOutlined, DeleteOutlined, PlusOutlined} from "@vicons/antd"
import TableOperationAreaButtonGroup from "@/components/TableOperationAreaButtonGroup.vue";

const {proxy} = getCurrentInstance();
const dialog = useDialog()
const message = useMessage()


let createRepoName = ref("")
let createRepoType = ref("")
let createRepoAddress = ref("")
let createRepoUsage = ref("")

let updateByType = ref("")
let updateByAddress = ref("")
let updateByUsage = ref("")

let repos = ref([])
let repoName = ref("")
let repoConnectTypeSelectOptionValue = ref(null)

let now_Row = ref("")

onMounted( () => {
  handleSearchAll()
})

function handleSearchAll() {
  proxy.$axios.get("/api/config_repo/", {}).then( r => {
    if (r.status === 200) {
      const content = r.data
      if (content["code"] === "10000") {
        const data = content["data"]
        let result = [];
        console.log("标记")
        console.log("data", data)
        data.map((item) => {
          result.push({
              "name": item["name"],
              "connect_type": item["connect_type"],
              "address": item["address"],
              "usage": item["usage"],
              "create_time": item["create_time"],
              "update_time": item["update_time"],
          })
        });

        repos.value = result;
      } else {
      }
    } else {
      console.error(r.status)
    }
  }).catch( (err) => {
    message.error(err)
  })
}

let repoConnectTypeSelectOptions = [
  {
    label: "全部",
    value: null
  },
  {
    label: "SSH",
    value: "SSH",
  },
  {
    label: "HTTP/HTTPS",
    value: "HTTP/HTTPS",
  },
]

let repoUsage = ref("")

let columns = [{
  type: "selection",
  fixed: "left"
}, {
  title: "名称",
  key: "name",
  fixed: "left",
}, {
  title: "类型",
  key: "connect_type",
  width: 100
}, {
  title: "地址",
  key: "address",
  width: 500
}, {
  title: "用途",
  key: "usage",
  resizable: true
}, {
  title: "添加时间",
  key: "create_time",
  width: 220
}, {
  title: "更新时间",
  key: "update_time",
  width: 220
}, {
    title: "操作",
    key: "op",
    render(row) {
      return h(
          TableOperationAreaButtonGroup, {
            isShowDetail: true,
            isShowModify: true,
            isShowDelete: true,
            onDetailButtonClicked: () => {
              isShowDetailModal.value = true;
            },
            onModifyButtonClicked: () => {
              isShowModifyModal.value = true;

              now_Row = row
            },
            onDeleteButtonClicked: () => {
            },
          }
      );
    },
    fixed: "right",
    width: 150
  },
];

let isShowAddModal = ref(false);
let isShowModifyModal = ref(false);
let isShowDetailModal = ref(false);

function onAddModalAfterLeave() {

}

function onModifyModalAfterLeave() {

}

function onDetailModalAfterLeave() {

}

function onAddModalOk() {
  isShowAddModal.value = false;

  let repoName = createRepoName.value
  let repoType = createRepoType.value
  let repoAddress = createRepoAddress.value
  let repoUsage = createRepoUsage.value

  proxy.$axios.put("/api/config_repo/", {
    name: repoName,
    type: repoType,
    address: repoAddress,
    usage: repoUsage
  }).then( (res) => {
    if (res.status === 200) {
      handleSearchAll()
      message.success("远程仓库创建成功！")
    }
  }).catch( err => {
    message.error("远程仓库创建失败")
  })
}

function onAddModalFailed() {
  isShowAddModal.value = false;
}

function onDetailModalOk() {
  isShowDetailModal.value = false;
}

function onModifyModalFailed() {
  isShowModifyModal.value = false;
}

function onModifyModalOk() {
  isShowModifyModal.value = false;

  let name = now_Row["name"]
  message.success(name)
  let update_type = updateByType.value
  let update_Address = updateByAddress.value
  let update_usage = updateByUsage.value

  proxy.$axios.put("/api/config_repo/" + name, {
    connect_type: update_type,
    address: update_Address,
    usage: update_usage,
  }).then(r => {
    if (r.status === 200) {
      message.success("数据更新成功！")
      handleSearchAll()
    }
  }).catch( err => {
    console.log(err)
    message.error("数据更新失败")})
}

function handleAddButtonClicked() {
  isShowAddModal.value = true;
}

function handleBatchDeleteButtonClicked() {
  dialog.warning({
    title: "批量删除",
    content: "即将删除 24 个条目, 是否继续?",
    positiveText: "确定",
    negativeText: "取消",
    onPositiveClick: () => {
      message.success("删除成功!")
    },
  })
}

const pagination = reactive({
  page: 1,
  pageSize: 10,
  showSizePicker: true,
  pageSizes: [5, 10, 20, 50, 100],
  onChange: (page) => {
    pagination.page = page;
  },
  onUpdatePageSize: (pageSize) => {
    pagination.pageSize = pageSize;
    pagination.page = 1;
  }
})


</script>

<style scoped>
.op-area {
  padding-top: 15px;
  padding-bottom: 15px;
  display: flex;
}

.repo-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
</style>