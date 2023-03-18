<template>
  <div class="group-mgmt-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>权限控制</n-breadcrumb-item>
          <n-breadcrumb-item>组</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <div class="op-area">
      <n-select style="width: 250px; margin-right: 10px;" size="medium" v-model:value="roleSelectOptionValue"
                :options="roleSelectOptions" placeholder="选择检索条件"/>
      <n-input v-model:value="useGroupnameOrUsageSearch" style="margin-right: 10px;" placeholder="按照组名或者用途搜索, 支持全文检索.." type="text"/>
      <n-tooltip placement="top" trigger="hover">
        <template #trigger>
          <n-button secondary tertiary circle style="margin-left: 5px" type="info"
                    @click="handleSearchButtonClicked">
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
          <n-button secondary tertiary circle style="margin-left: 5px" type="success"
                    @click="handleInsertButtonClicked">
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
          <n-button secondary tertiary circle style="margin-left: 5px" type="error" @click="handleBatchEmptyButtonClicked">
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
    <n-data-table striped :columns="columns" :data="groups" :pagination="pagination" />
    <n-modal v-model:show="isShowAddModal" :mask-closablef="false" preset="card" title="添加组"
             :on-after-leave="onAddModalAfterLeave" :segmented="false" style="width: 45%; min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">名称</div>
          <n-input v-model:value="useTargetNameCreate" type="text" placeholder="必填, 请输入名称" style="margin-bottom: 10px; max-width: 200px"/>
          <div style="font-size: 12pt; font-weight: bold;">用途</div>
          <n-input v-model:value="useUsageCreate" type="text" placeholder="请输入用途"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onAddModalFailed" style="margin-right: 10px;">取&nbsp;消</n-button>
          <n-button @click="onAddModalOk" type="primary">添&nbsp;加</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal v-model:show="isShowModifyModal"
             :mask-closablef="false"
             preset="card"
             title="修改组"
             :on-after-leave="onModifyModalAfterLeave"
             :segmented="false"
             style="width: 45%;
             min-width: 600px">
      <div style="display: flex;width: 100%; height: 100%; flex-direction: column">
        <div style="width: 100%; ">
          <div style="font-size: 12pt; font-weight: bold;">用途</div>
          <n-input v-model:value="useUsageInput" type="text" placeholder="请输入用途"/>
        </div>
        <div style="display: flex; width: 100%; height: 100%; justify-content: flex-end; margin-top: 10px">
          <n-button @click="onModifyModalFailed" style="margin-right: 10px;">取&nbsp;消</n-button>
          <n-button @click="onModifyModalOk" type="primary">修&nbsp;改</n-button>
        </div>
      </div>
    </n-modal>
    <n-modal
        v-model:show="isShowDeleteModal"
        :mask-closable="false"
        preset="dialog"
        title="危险操作"
        content="这是一个危险的操作，你确认要删除这个数据吗？"
        positive-text="确认"
        negative-text="取消"
        @positive-click="onPositiveClick"
        @negative-click="onNegativeClick"
    />
    <div style="width: 100%; min-height: 20px;"></div>
  </div>
</template>

<script setup>
import {h, reactive, ref, getCurrentInstance, onMounted, } from "vue";
import {NButton, useDialog, useMessage} from "naive-ui";
import {SearchOutlined, CloseOutlined, DeleteOutlined, PlusOutlined} from "@vicons/antd"
import TableOperationAreaButtonGroup from "@/components/TableOperationAreaButtonGroup.vue";

const {proxy} = getCurrentInstance();
const dialog = useDialog();
const message = useMessage();
const useGroupnameOrUsageSearch = ref("");
const useTargetNameCreate = ref("");
const useUsageCreate = ref("");
const showModalRef = ref(false);
const useUsageInput = ref("")

let nowRow = ref()
let roleSelectOptionValue = ref(null)

onMounted(() => {
  proxy.$axios.get("/api/group/", {}).then(r => {
    if (r.status === 200) {
      const content = r.data
      if (content["code"] === "10000") {
        const data = content["data"]
        let result = [];

        data.map((item) => {
          result.push({
            "key": item["name"],
            "name": item["name"],
            "create-time": item["create_time"],
            "update-time": item["update_time"],
            "usage": item["usage"]
          })
        });

        groups.value = result;
      } else {
      }
    } else {
      console.error(r.status)
    }
  }).catch(e => {
  })
})

let roleSelectOptions = [
  {
    label: "全部",
    value: null
  }, {
    label: "名称",
    value: "名称"
  }, {
    label: "用途",
    value: "用途"
  },
]

let isShowAddModal = ref(false);
let isShowModifyModal = ref(false);
let isShowDeleteModal = ref(false);


function onAddModalAfterLeave() {
}

function onModifyModalAfterLeave() {
}

function onAddModalOk() {
  handleInsertButtonClicked()
  isShowAddModal.value = false;

  let createName = useTargetNameCreate.value
  let createUsage = useUsageCreate.value

  proxy.$axios.post("/api/group/", {
    name: createName,
    usage: createUsage,
  }).then(c => {
    if (c.status === 200) {
      handleSearchButtonClicked()
    }
  }).catch(e => {
  })
}

function onAddModalFailed() {
  isShowAddModal.value = false;
}

function onModifyModalFailed() {
  isShowModifyModal.value = false;
}

function onModifyModalOk() {
  isShowModifyModal.value = false;

  let condition = nowRow["name"]
  let usage_input = useUsageInput.value

  proxy.$axios.put("/api/group/update_group", {
    new_usage: usage_input,
    document_condition: condition,
  }).then( (res) => {
        if (res.status === 200) {
          handleSearchButtonClicked()
        }
      }).catch(err => {
        console.log(err)
  })
}

function handleSearchButtonClicked() {
  let inputVal = useGroupnameOrUsageSearch.value
  proxy.$axios.get("/api/group/" + inputVal, {
  }).then( r => {
    if (r.status === 200) {
      const content = r.data
      console.log("搜索成功！")
      if (content["code"] === "10000") {
        const data = content["data"]
        let result = [];

        data.map((item) => {
          result.push({
            "key": item["name"],
            "name": item["name"],
            "create-time": item["create_time"],
            "update-time": item["update_time"],
            "usage": item["usage"]
          })
        });

        groups.value = result;
      } else {
      }
    } else {
      console.error(r.status)
    }
  }).catch(e => {
  })
}

function handleInsertButtonClicked() {
  isShowAddModal.value = true
}

function handleBatchEmptyButtonClicked() {
  useGroupnameOrUsageSearch.value = ''
}

function onPositiveClick() {

  let deleteName = nowRow["name"]
  console.log(deleteName)
  proxy.$axios.delete("/api/group/useNameDelete", {
    params: {
      name: deleteName,
    }
  }).then(c => {
    if (c.status === 200) {
      handleSearchButtonClicked()
      message.success("数据删除成功");
    }
  }).catch(e => {
    message.success("数据删除失败");
    console.log(e)
  })
}

function handleBatchDeleteButtonClicked() {
  dialog.warning({
    title: "批量删除",
    content: "即将删除 24 个条目, 是否继续?",
    positiveText: "确定",
    negativeText: "取消",
    onPositiveClick: () => {
      message.success("删除成功")
    },
  })
}

function handleDeleteButtonOnClickedOne() {
  return {
    isShowDeleteModal: showModalRef,
    onNegativeClick() {
      message.success("已取消删除操作");
      showModalRef.value = false;
    },
    onPositiveClick() {
      message.success("数据删除成功");
      showModalRef.value = false;
    }
  };
}

let groups = ref([])


let columns = [
  {
    type: "selection",
    fixed: "left"
  }, {
    title: "组名",
    key: "name",
    fixed: "left",
    width: 250
  }, {
    title: "创建时间",
    key: "create-time",
    width: 200

  }, {
    title: "更新时间",
    key: "update-time",
    width: 200
  },{
    title: "用途",
    key: "usage",
    resizable: true,
  }, {
    title: "操作",
    key: "op",
    render(row) {
      return h(
          TableOperationAreaButtonGroup, {
            isShowDetail: false,
            isShowModify: true,
            isShowDelete: true,
            onDetailButtonClicked: () => {
            },
            onModifyButtonClicked: () => {
              isShowModifyModal.value = true
              nowRow = row
            },
            onDeleteButtonClicked: () => {
              isShowDeleteModal.value = true
              nowRow = row
            },
          }
      )
    },
  }
]

const pagination = reactive({
  page: 1, // 默认在第几页
  pageSize: 5, //每页的行数
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

.group-mgmt-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
</style>